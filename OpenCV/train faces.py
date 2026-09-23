import os
import cv2 as cv
import numpy as np

people = ['Ben Affleck', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
dir =r'/Users/murugan/Desktop/OpenCV/Faces'

haar_Casacade = cv.CascadeClassifier('haar face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(dir, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_read = cv.imread(img_path)
            gray = cv.cvtColor(img_read, cv.COLOR_BGR2GRAY)
            cv.imshow('Gray', gray)

            faces_rect = haar_Casacade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                faces_region = gray[y:y+h, x:x+w]
                features.append(faces_region)
                labels.append(label)

create_train()    
print('training done -------------')

features = np.array(features, dtype='object')
labels = np.array(labels, )

face_recogniser = cv.face.LBPHFaceRecognizer_create()

face_recogniser.train(features,labels)

face_recogniser.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels'
'.npy', labels) 