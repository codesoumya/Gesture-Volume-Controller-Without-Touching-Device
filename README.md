# Volume Hand Control

A Python-based application that allows users to control the system volume using hand gestures via a webcam. The project utilizes OpenCV, MediaPipe, and Pycaw for hand tracking and audio control.

---

## Features
- **Real-Time Hand Tracking**: Tracks the user's hand and identifies key landmarks.
- **Volume Control**: Adjusts the system volume based on the distance between the thumb and index finger.
- **Customizable Settings**: Modify detection confidence, tracking confidence, and other parameters to suit your needs.

---

## Installation

### Prerequisites
Ensure you have Python installed on your system. Then, install the required packages by running the following commands:

```bash
pip install opencv-python
pip install numpy
pip install mediapipe
pip install pycaw
```

### Clone the Repository
Clone this project from GitHub:

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

---

## Usage

1. Connect your webcam to your computer (use `0` for the inbuilt webcam, or update the code to use an external webcam).
2. Run the main script:

```bash
python volume_hand_control.py
```

3. Follow these gestures to control the volume:
   - Move your thumb and index finger closer or farther apart to adjust the system volume.
   - Ensure your hand is visible and properly detected by the webcam.

---

## Project Structure

```
.
├── volume_hand_control.py      # Main application script
├── handTracxkingModule.py      # Hand tracking module
└── README.md                   # Project documentation
```

---

## Code Explanation

### `volume_hand_control.py`
- Captures video from the webcam.
- Uses the `handTracxkingModule` to detect hand landmarks.
- Calculates the distance between the thumb tip and index finger tip to control the system volume.

### `handTracxkingModule.py`
- A reusable module for hand detection and landmark identification using MediaPipe.
- Provides methods to detect hands and extract position information of key hand landmarks.

---

## Dependencies

- [OpenCV](https://opencv.org/): For video capture and image processing.
- [NumPy](https://numpy.org/): For mathematical computations.
- [MediaPipe](https://mediapipe.dev/): For efficient hand detection and tracking.
- [Pycaw](https://github.com/AndreMiras/pycaw): For system audio control.

---

## Customization

- **Hand Tracking Settings**: Adjust the detection and tracking confidence levels in `handTracxkingModule.py` by modifying the `detectionCon` and `trackCon` parameters.
- **Volume Sensitivity**: Modify the volume range or the standard scaling factor in `volume_hand_control.py` for finer control.

---

## Troubleshooting

- If the webcam feed does not start, ensure your webcam is connected and accessible.
- For external webcams, change `cv2.VideoCapture(0)` to the appropriate device index.
- Ensure all dependencies are installed correctly.

---

## Author
**Soumyadip Bhattacharyya**

- **Email**: [soumyadipbppimt@gmail.com](mailto:soumyadipbppimt@gmail.com)
- **WhatsApp**: +918918713314

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- MediaPipe by Google for their efficient hand-tracking solution.
- Pycaw for providing a simple way to interact with the Windows Audio API.

Feel free to contribute or report issues! 😊
