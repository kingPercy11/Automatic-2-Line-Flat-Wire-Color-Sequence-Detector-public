import cv2
import numpy as np
import simpleaudio as sa

def remove_background(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    binary = cv2.bitwise_not(binary)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_area = 100
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
    contour_image = np.zeros_like(gray)
    cv2.drawContours(contour_image, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
    result = cv2.bitwise_and(image, image, mask=contour_image)
    return result


thresholds = [
    [160, 179, 100, 255, 100, 255],  # red
    [5, 15, 100, 255, 100, 255],  # orange
    [40, 80, 50, 255, 50, 250],  # green
    [20, 40, 100, 255, 100, 255],  # yellow
    [105, 113, 100, 250, 50, 150],  # blue
    [100, 120, 100, 250, 100, 250]  # violet
    # more wire shades(l hue u hue l saturation u saturation l bright u bright) can be added there

]


def color_detection(image, threshold, index):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_hue, upper_hue, lower_saturation, upper_saturation, lower_value, upper_value = threshold[index]
    lower_bound = np.array([lower_hue, lower_saturation, lower_value], dtype=np.uint8)
    upper_bound = np.array([upper_hue, upper_saturation, upper_value], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(image, image, mask=mask)
    # cv2.imshow('Original Image', image)
    # cv2.imshow('Color Detection Result', result)
    x_coord = None
    for x in range(mask.shape[1]):
        column = mask[:, x]
        if cv2.countNonZero(column) > 0:
            x_coord = x
            break
    cv2.waitKey(2)
    return x_coord


def position(image, threshold):
    length = len(threshold)
    x_coor = []
    for i in range(length):
        pos = color_detection(image, threshold, i)
        x_coor.append(pos)
    return x_coor


def check_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return i
    return "Correct"


# def play_alarm():
#     wave_obj = sa.WaveObject.from_wave_file("/Users/pranjal/Downloads/youtube_72937.wav")
#     wave_obj.play()

color=["red","orange", "green", "yellow", "blue", "violet"]
image_path = input("Enter the image path: ")
result = remove_background(image_path)
ans = position(result, thresholds)
print("wire number with problem:", check_sorted(ans))
print (color[check_sorted(ans)])
# if(check_sorted(ans)!="Correct"):
#     play_alarm()

# import sounddevice as sd
# print(sd.query_devices())
