# -*- coding: utf-8 -*-


# Commented out IPython magic to ensure Python compatibility.
# !nvidia-smi
import os

HOME = os.getcwd()
print(HOME)
# %cd {HOME}

# !pip3 install cmake
# !pip3 install setuptools
# !pip3 install dlib
# !pip3 install face-recognition
# !pip3 install opencv-python

import face_recognition
import cv2
import time


def append_time_to_filename(filename):
    # Get the current time in "hh-mm-ss" format
    current_time = time.strftime("%H-%M-%S")
    # Split the filename and extension
    name, ext = filename.rsplit(".", 1)
    # Create the new filename by appending the current time
    new_filename = f"{name}_{current_time}.{ext}"
    print(f"New file name is = {new_filename}")
    return new_filename


# Open the input movie file
input_movie = cv2.VideoCapture(f"{HOME}/aniket-video-shorter.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
# fourcc = cv2.VideoWriter_fourcc(*"X264")
# output_movie = cv2.VideoWriter("output2.avi", fourcc, 24, (1280, 720))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # or use "X264"
output_movie = cv2.VideoWriter(
    append_time_to_filename("output.mp4"), fourcc, 24, (1280, 720)
)

# Load some sample pictures and learn how to recognize them.
aniket_image = face_recognition.load_image_file(f"{HOME}/Identity-1.png")
aniket_face_encoding = face_recognition.face_encodings(aniket_image)[0]
known_faces = [aniket_face_encoding]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0
batch_size = 64
frames = []
frame_count = 0
match_found = False
while True:
    ret, frame = input_movie.read()
    # break when video ends
    if not ret:
        break

    frame_count += 1
    frames.append(frame)
    if len(frames) == batch_size:
        match_found = False
        batch_of_face_locations = face_recognition.batch_face_locations(
            frames, number_of_times_to_upsample=0, batch_size=batch_size
        )
        for frame_number_in_batch, face_locations in enumerate(batch_of_face_locations):
            number_of_faces_in_frame = len(face_locations)

            frame_number = frame_count - batch_size + frame_number_in_batch
            if number_of_faces_in_frame >= 1:
                print(
                    f"I found {number_of_faces_in_frame} face(s) in frame #{frame_number}."
                )

                current_frame = frames[frame_number_in_batch]
                face_encodings = face_recognition.face_encodings(
                    current_frame, face_locations
                )
                for face_encoding in face_encodings:
                    match = face_recognition.compare_faces(
                        known_faces, face_encoding, tolerance=0.50
                    )
                    if match[0]:
                        # load all 64 frames in output file
                        match_found = True
                        print("Aniket found")
                        for i in range(batch_size):
                            output_movie.write(frames[i])
                        frames = []
                        break
            if match_found:
                break
        frames = []
        print("next batch")

input_movie.release()
output_movie.release()
cv2.destroyAllWindows()
