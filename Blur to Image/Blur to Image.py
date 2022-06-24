import cv2  # pip install opencv-python

image = cv2.imread("blur3.png")
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedBlur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedBlur, scale=200.0)

cv2.imwrite("Sketch_blur3.png", sketch)
