import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Face Cascade file is present in "C:\Users\kumar\Desktop\C0d3\.py\Open_CV_AMS\cascades\data"
face_cascade = cv2.CascadeClassifier('C:\\Users\\kumar\\Desktop\\C0d3\\.py\\Open_CV_AMS\\cascades\\data\\haarcascade_frontalface_alt2.xml')
# eye_cascade = cv2.CascadeClassifier('C:\\Users\\kumar\\Desktop\\C0d3\\.py\\Open_CV_AMS\\cascades\\data\\haarcascade_eye.xml')
# face_cascade = cv2.CascadeClassifier('cascades\\data\\haarcascade_frontalface_alt2.xml')
# eye_cascade = cv2.CascadeClassifier('cascades\\data\\haarcascade_eye.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here 
    GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(GRAY, scaleFactor = 1.5, minNeighbors = 5)
    # minSize=(20, 20)
    for(x, y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = GRAY[y:y+h, x:x+w]
        roi_color = GRAY[y:y+h, x:x+w]
        img_item = "abhishek_pic.png"
        cv2.imwrite(img_item, roi_gray)
# Detecting EYES

        color = (0, 0, 255)#BGR 0-255
        stroke = 2
        width = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for(ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(roi_color, (ex, ey), (ex+ew,ey+eh), (0, 255, 0), 2)


# Display the resulting frame
    cv2.imshow('Normal Frame', frame)
    # cv2.imshow('gray', GRAY)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
# and destoy all the windows
cv2.destroyAllWindows()


















# import numpy as np
# import cv2
# # import pickle

# face_cascade = cv2.CascadeClassifier(
#     'cascades/data/haarcascade_frontalface_alt2.xml')
# eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')


# # recognizer = cv2.face.LBPHFaceRecognizer_create()
# # recognizer.read("./recognizers/face-trainner.yml")

# # labels = {"person_name": 1}
# # with open("pickles/face-labels.pickle", 'rb') as f:
# #     og_labels = pickle.load(f)
# #     labels = {v: k for k, v in og_labels.items()}

# cap = cv2.VideoCapture(0)

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(
#         gray, scaleFactor=1.5, minNeighbors=5)
#     for (x, y, w, h) in faces:
#         print(x,y,w,h)
#         roi_gray = gray[y:y+h, x:x+w]  # (ycord_start, ycord_end)
#         roi_color = frame[y:y+h, x:x+w]

#         # recognize? deep learned model predict keras tensorflow pytorch scikit learn
#         # id_, conf = recognizer.predict(roi_gray)
#         # if conf >= 4 and conf <= 85:
#             # print(5: #id_)
#             # print(labels[id_])
#         #     font = cv2.FONT_HERSHEY_SIMPLEX
#         #     name = labels[id_]
#         #     color = (255, 255, 255)
#         #     stroke = 2
#         #     cv2.putText(frame, name, (x, y), font, 1,
#         #                 color, stroke, cv2.LINE_AA)

#         # img_item = "7.png"
#         # cv2.imwrite(img_item, roi_color)

#         # color = (255, 0, 0)  # BGR 0-255
#         # stroke = 2
#         # end_cord_x = x + w
#         # end_cord_y = y + h
#         # cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
#         #subitems = smile_cascade.detectMultiScale(roi_gray)
#         # for (ex,ey,ew,eh) in subitems:
#         #	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
