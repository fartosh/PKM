import cv2
import numpy as np


cap = cv2.VideoCapture("strzyza1.mp4")
print("Liczba ramek:", int(cap.get(7)))

ret, base = cap.read()
if not ret:
    print("Nie mozna wczytac klatki")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Nie mozna wczytac klatki")
        break

    buf = cv2.subtract(base, frame)
    title = str(cap.get(0)/1000) + " s"
    sum = np.sum(buf, axis=2)

    if np.amax(sum) > 600:
        cv2.imshow("Klatka", frame)
        print("Czas:", title)
        print("Maksymalna wartosc:", np.amax(sum))

        while not cv2.waitKey(1) & 0xFF == ord('q'):
            pass

cap.release()
cv2.destroyAllWindows()
