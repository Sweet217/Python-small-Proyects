import cv2
import os
import imutils

#Automatization of directories
personName = input('Dime tu nombre: ')
dataPath = 'C:\\Users\\soyel\\Desktop\\Proyectos propios\\Hotel-database-Manipulation\\Face recognition project\\Database'
personPath = os.path.join(dataPath, personName)

if not os.path.exists(personPath):
    print('Carpeta Creada: ', personPath)
    os.makedirs(personPath)

#Frame opening and closing
videoCapture = cv2.VideoCapture(0)

faceClassification = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
count = 0

while True:
    ret, frame = videoCapture.read()
    if not ret:
        break
    frame = imutils.resize(frame, width = 400)

    if frame.shape[0] == 0 or frame.shape[1] == 0:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxiliarFrame = frame.copy()

    faces = faceClassification.detectMultiScale(gray, 1.3, 5)

    # Loop over each face in the list of detected faces
    for (x, y, w, h) in faces:

    # Draw a rectangle around the face using the bounding box coordinates
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Extract the region of the input frame that corresponds to the detected face
        face = auxiliarFrame[y:y + h, x:x + w]
    # Resize the extracted face image to a fixed size of (720, 720) pixels
        face = cv2.resize(face, (128, 128), interpolation=cv2.INTER_CUBIC)
    # Save the extracted and resized face image to a file in the person's directory
        cv2.imwrite(personPath + '/face_{}.jpg'.format(count), face)
    # Increment the face count by 1
        count = count + 1

    cv2.imshow('frame', gray)

    #Close with escape key or if count its more or equal than 300
    closeKey = cv2.waitKey(1)
    if closeKey == 27 or count >= 300:
        break
    

videoCapture.release()
cv2.destroyAllWindows()