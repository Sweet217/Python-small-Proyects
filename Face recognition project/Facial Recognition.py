import cv2
import os

dataPath = 'C:\\Users\\soyel\\Desktop\\Proyectos propios\\Hotel-database-Manipulation\\Face recognition project\\Database'
imagePath = os.listdir(dataPath)
print('imagePath= ', imagePath)

faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

faceRecognizer.read('C:/Users/soyel/Desktop/Proyectos propios/Hotel-database-Manipulation/Face recognition project/Xml Files/training.xml')

capture = cv2.VideoCapture(0)

faceClassification = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = capture.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxiliarFrame = gray.copy()

    if frame.shape[0] == 0 or frame.shape[1] == 0:
        continue

    faces = faceClassification.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        facial = auxiliarFrame[y:y + h, x:x + w]
        facial = cv2.resize(facial, (100, 100), interpolation=cv2.INTER_CUBIC)
        result = faceRecognizer.predict(facial)
        cv2.putText(frame, '{}'.format(result), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)

        if result[1] < 5800:
            cv2.putText(frame, '{}'.format(imagePath[result[0]]), (x,y-25),2,1.1,(0,255,0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2) 
        else:
            cv2.putText(frame, 'unknow', (x,y-20), 2, 0.8, (0,0,255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x,y), (x+w), (y+h), (0,0,255), 2)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
