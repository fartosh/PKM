import cv2

print(cv2.__version__)

cap = cv2.VideoCapture("strzyza.mp4")
ret, img = cap.read()
print(type(img))

img0 = cv2.imwrite("image.png", img)
cv2.waitKey(0)
