# RealityTV-Savior
This script saves you from the trauma of having to watching Reality TV
# Face Recognition Video Batch Processor

This script processes video files to identify frames containing a specific face using the Face Recognition library and OpenCV. When the target face (in this example, "Aniket") is detected in a batch of video frames, the entire batch is written to an output video file with a timestamp appended to its filename.

## Overview

The script performs the following tasks:

- Reads a video file from the current working directory.
- Loads a reference image (`Identity-1.png`) and computes its face encoding.
- Processes the video in batches (default batch size: 64 frames) for efficiency.
- Uses the `face_recognition` library to detect faces in each batch.
- Compares detected faces against the known face.
- When a match is found (using a tolerance of 0.50), writes the entire batch of frames to an output video file. The output filename includes the current time stamp.
- Releases all video objects and cleans up OpenCV windows when processing is complete.


## Dependencies

Ensure that your Python environment (Python 3.x) has all the required libraries installed:

- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python)
- [face_recognition](https://pypi.org/project/face-recognition)
- [dlib](http://dlib.net/) (required by face_recognition)
- [cmake](https://cmake.org/) (sometimes required to build dlib)
- [setuptools](https://pypi.org/project/setuptools/)

You can install the necessary packages using pip. For example:

```bash
pip install cmake setuptools dlib face_recognition opencv-python
```

_Notes:_

- Some systems might require additional build tools for installing `dlib`.
- If you encounter issues, consult the documentation for each package.


## How It Works

1. **Setup and Input**
The script first determines the current working directory (`HOME`) and uses it to locate the input video (`aniket-video-shorter.mp4`) and the reference image (`Identity-1.png`).
2. **Appending Timestamp to Filename**
The function `append_time_to_filename(filename)` takes a base filename and appends the current time (formatted as "HH-MM-SS") to make the output file unique.
3. **Video Processing in Batches**
The video is read frame-by-frame into batches of 64 frames. For each batch:
    - Batch face locations are computed.
    - Each detected face is encoded.
    - The face encoding is compared to the known face encoding with a tolerance value of 0.50.
    - If a match occurs in any frame, the entire batch is written to the output video.
4. **Output Video**
The output video is written using OpenCV’s `VideoWriter` with a resolution of 1280×720 and a frame rate of 24 fps. The codec used is `"mp4v"` (or you can change it based on your needs).

## Usage

1. Place your video file (`aniket-video-shorter.mp4`) and reference image (`Identity-1.png`) in the same directory as the script, or adjust the file paths accordingly.
2. Run the script with Python:

```bash
python your_script_name.py
```

3. When a matching face is detected in a batch of frames, the script writes those frames to an output file (e.g., `output_12-34-56.mp4`).
4. Once processing is complete, the script automatically releases the video objects and destroys OpenCV windows.

## Customization

- **Batch Size:**
Adjust the `batch_size` variable if you want to process larger or smaller groups of frames at once.
- **Face Detection Tolerance:**
Modify the tolerance parameter in the `face_recognition.compare_faces` function for a more or less strict matching criterion.
- **Output Video Settings:**
Change the four-character code (`fourcc`), frame rate, or resolution in the `cv2.VideoWriter` as needed to suit your input video's properties.


## Troubleshooting

- Make sure that the input files (`aniket-video-shorter.mp4` and `Identity-1.png`) exist in the specified directory.
- Verify that your Python environment has all the necessary dependencies installed.
- If you experience performance issues with face detection, consider experimenting with the `number_of_times_to_upsample` parameter in the `batch_face_locations` function.


## License

This project is open source and available for modification and redistribution under your preferred license. (Specify your license if needed.)

## Acknowledgments

- [Face Recognition](https://github.com/ageitgey/face_recognition) library by Adam Geitgey
- [OpenCV](https://opencv.org/)
- Various open-source contributors

------------------------------------------------------------

This documentation should help users to understand the script's functionality, install the required packages, and customize the code as per their requirements. Enjoy processing your videos with face recognition!

