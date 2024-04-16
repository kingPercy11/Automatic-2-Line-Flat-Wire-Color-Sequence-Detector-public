* Background Removal:
        The remove_background function takes an image as input, converts it to grayscale, and applies Gaussian blur to reduce noise.
        It then uses Otsu's thresholding to create a binary image, which is inverted. 
        Contours are then found in the binary image, and a minimum area threshold is applied to filter out small contours. 
        Finally, a mask is created based on the contours, and the original image is bitwise ANDed with the mask to remove the background.

* Color Detection: 
        The color_detection function takes the processed image and a threshold for a specific color. 
        It converts the image to HSV format and applies the threshold to create a mask for the specified color. 
        It then finds the x-coordinate of the first non-zero pixel in the mask, which represents the position of the color in the image.

* Position Detection:
        The position function iterates over the list of color thresholds and calls color_detection for each color.
        It collects the x-coordinates of the colors in a list and returns it.

* Sorting Check: 
        The check_sorted function takes the list of x-coordinates and checks if they are in ascending order. 
        If a deviation is found, it returns the index of the first out-of-order element.

* Alarm Sound:
        The play_alarm function plays an alarm sound using the simpleaudio library. 
        It loads a WAV file and plays it when called.
                  
* Main Process:
        The main part of the code prompts the user for an image path, 
        removes the background,
        detects the position of each color, 
        checks if the colors are sorted correctly,
        and prints the result. 
        If the colors are not sorted correctly, it plays an alarm sound.
