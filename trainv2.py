import cv2 as cv
import os, random
import numpy as np

mask_types = ['with_mask', 'without_mask', 'mask_weared_incorrect' ]
DIR = r'./Samples'

features = []
labels = []

def train():
    for i in mask_types:
        path = os.path.join(DIR, i)
        mask_type = mask_types.index(i)
        
        if i == 'with_mask':
            for img in os.listdir(path):
                if random.randint(1,18) == 1:
                    img_path = os.path.join(path, img)
                    img_array = cv.imread(img_path)
                    gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
                    
                    features.append(gray)
                    labels.append(mask_type)
        else:
            for img in os.listdir(path):
                if random.randint(1,3) == 1:
                    img_path = os.path.join(path, img)
                    img_array = cv.imread(img_path)
                    gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
                    
                    features.append(gray)
                    labels.append(mask_type)

train()
print('---------------Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

print("Length of features: ", len(features))
print("Length of labels: ", len(labels))


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

face_recognizer.save('trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
