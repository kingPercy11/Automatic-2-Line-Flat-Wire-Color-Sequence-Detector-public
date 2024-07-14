# Wire Position Checker

Wire Position Checker is a Python script that detects specific colored wires in an image, checks their positions, and determines if they are in the correct order. If a wire is found to be out of order, the script can visually mark the position with a cross.

## Features

- Detects specific colored wires in an image.
- Removes the background from the image.
- Checks the positions of detected wires and verifies if they are in the correct order.
- Visually marks the position of any wire that is out of order.
- Can play an alarm sound if a wire is out of order (currently commented out).

## Prerequisites

- Python 3.x
- `opencv-python`
- `numpy`
- Optionally: `simpleaudio` for playing alarm sounds (commented out)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/wire-position-checker.git
    cd wire-position-checker
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python numpy
    ```

3. Optionally, install `simpleaudio` if you want to enable the alarm sound:
    ```bash
    pip install simpleaudio
    ```

## Usage

1. Prepare your images:
    - An image of the wires with the background removed.
    - An image of the actual wires with the background.

2. Run the script:
    ```bash
    python wire_position_checker.py
    ```

3. Input the path to the image with the background removed when prompted.

4. The script will detect the wires and check their positions. If a wire is out of order, it will mark the position with a red cross and display the image.

5. Optionally, if the alarm sound is enabled, it will play if a wire is out of order.

## Code Explanation

- `remove_background(image_path)`: Removes the background from the image using contour detection.
- `color_detection(image, threshold, index)`: Detects a specific color in the image and returns the x-coordinate of the first pixel that matches the color.
- `position(image, threshold)`: Gets the positions of all specified colors in the image.
- `check_sorted(arr)`: Checks if the positions of the wires are in the correct order.
- `draw_cross(image, x_coord)`: Draws a red cross at the specified x-coordinate.
- `play_alarm()`: Plays an alarm sound (currently commented out).

## Future Additions

- Enabling a menu option to choose from various threshold values for different colored wires.
- Implementing additional features for better wire detection and sorting.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to submit issues and enhancement requests.

## Acknowledgements

- This project uses [OpenCV](https://opencv.org/) for image processing.
- This project uses [NumPy](https://numpy.org/) for numerical operations.
- Optionally, this project can use [simpleaudio](https://simpleaudio.readthedocs.io/en/latest/) for playing sounds.
