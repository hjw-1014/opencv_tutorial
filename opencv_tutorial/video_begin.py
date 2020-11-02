# generate video and save it

import cv2
import datetime

cap = cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# cap.set(3, 3000)
# cap.set(4, 3000)
# print(cap.get(3))
# print(cap.get(4))


fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D') #(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

print(cap.isOpened())

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width:' + str(cap.get(3)) + ' Height:' + str(cap.get(4))
        datet = str(datetime.datetime.now())

        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0,255,255), 2, lineType=cv2.LINE_AA)
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        out.write((frame))

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
        #
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

