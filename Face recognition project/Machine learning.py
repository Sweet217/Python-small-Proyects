import cv2
import os
import numpy as np

#Creation of the list of people that the database have
dataPath = 'C:\\Users\\soyel\\Desktop\\Proyectos propios\\Hotel-database-Manipulation\\Face recognition project\\Database'
peopleList = os.listdir(dataPath)
print('People list', peopleList)

labels = []
facesData = []
labelCount = 0

for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir
    print('Reading Images')

    for fileName in os.listdir(personPath):
        print('Faces: ', nameDir + '/' + fileName)
        labels.append(labelCount)

        facesData.append(cv2.imread(personPath + '/' + fileName, 0))
        image = cv2.imread(personPath + '/' + fileName, 0)


        #IMAGES MINI TEST
        #cv2.imshow('image', image)
        #cv2.waitKey(10)
    labelCount = labelCount + 1

#cv2.destroyAllWindows()

#print('labels =', labels)
#print('Number of labels', np.count_nonzero(np.array(labels)==0))
#print('Number of labels', np.count_nonzero(np.array(labels)==1))

#Machile learning method selected : LBPHF or Fisher
faceRecognizer = cv2.face_LBPHFaceRecognizer.create()

print('___Training in process___')
faceRecognizer.train(facesData, np.array(labels))

pathToSave = 'C:/Users/soyel/Desktop/Proyectos propios/Hotel-database-Manipulation/Face recognition project/Xml Files/training.xml'


faceRecognizer.write(pathToSave)
print('Model Saved')

