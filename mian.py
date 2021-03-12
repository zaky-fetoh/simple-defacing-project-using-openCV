import cv2 as cv


cap = cv.VideoCapture('John.mp4')
if cap.isOpened() == False:
    print("noile")

cv.namedWindow("john")
face = cv.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')


def detect_face(frame):
    return frame


while True:

    ret, frame = cap.read()

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    elif ret:
        #print(frame.shape, frame.dtype)
        frame = cv.UMat( frame[::2, ::2, :])
        rects = face.detectMultiScale(frame)
        for x, y, w, h in rects:
            print(x, y, h, w)
            cv.rectangle(frame, (x, y), (x + w, y + h),
                         color=(255,0,0), thickness=-1)
        cv.imshow("john", frame)
    else:
        break

cap.release()
cv.destroyAllWindows()
