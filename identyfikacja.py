import cv2


filename = "vid/strzyza6.mp4"

camera = cv2.VideoCapture(filename)
i = 0
timestamps = 0
check = int(0.1*camera.get(7))

for i in range(20):
    i += 1
    ret, frame = camera.read()

cv2.imshow(str(timestamps), frame)
timestamps = camera.get(0) / 1000
while not cv2.waitKey(0):
    pass

cv2.imwrite("frame20.jpg", frame)

print(frame.shape)
mask = frame[828:860, 723:755, :]
cv2.imwrite("mask1.jpg", mask)

camera.set(1, check)
_, check_frame = camera.read()
timestamps = camera.get(0) / 1000
cv2.imwrite("check.jpg", check_frame)

result = cv2.matchTemplate(check_frame, mask, method=1)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED (0, 1)
top_left = min_loc

#others
#top_left = max_loc

bottom_right = (top_left[0] + 32, top_left[1] + 32)
cv2.rectangle(check_frame, top_left, bottom_right, 255, 2)


cv2.imshow(str(timestamps), check_frame)
while not cv2.waitKey(0):
    pass

camera.release()
cv2.destroyAllWindows()