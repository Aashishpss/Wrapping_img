Image Wrapping on Mouse Click

This project allows users to select four points on an image by clicking with the mouse. Once four points are selected, the program performs a perspective transformation, "wrapping" the image to a rectangular shape based on the clicked points.
Features

    Interactive Mouse Clicks: Click on the image to select four points, which will be used for the perspective transformation.
    Perspective Transformation: The selected points are used to warp the image into a rectangle.
    Real-time Preview: The program shows the original image and the transformed image after clicking the four points.

Installation

    Clone this repository to your local machine.

git clone https://github.com/yourusername/image-wrapping.git
cd image-wrapping

Install the necessary dependencies.

    pip install opencv-python numpy

Usage

    Place the image (scan_test2.jpg) in the project directory.

    Run the script.

    python image_wrapping.py

    Click four points on the image in the order: top-left, top-right, bottom-right, bottom-left. The image will be wrapped according to these points.

    Press '1' to close the program after the transformation.

Code Overview
1. Image Loading and Resizing

The image is loaded using OpenCV, and resized for better performance.
2. Mouse Click Event

    A mouse callback function is used to capture the coordinates of the points clicked by the user.
    The coordinates of the four points are stored in a list.

3. Reordering Points

    A helper function reorder() takes the list of points and arranges them in the correct order: top-left, top-right, bottom-right, and bottom-left.

4. Perspective Transformation

    After selecting the points, a perspective transformation matrix is calculated using the selected points and applied to the image using OpenCV’s cv2.warpPerspective() function.

5. Displaying the Output

    The program shows the original image with circles marking the clicked points and the transformed image in a separate window.
