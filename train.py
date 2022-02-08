import cv2 as cv
import json, os
import numpy as np

mask_type = ['with_mask', 'without_mask', 'mask_weared_incorrect' ]
DIR = r'./Samples'

features = []
labels = []

def create_train(imagefile):
    img = cv.imread('./images/'+ imagefile)
    
    jsonFileName = imagefile.split('.')[0] + '.xml.json'
    with open("./jsons/" + jsonFileName) as json_file:
        data = json.load(json_file)

    boxes = data["annotation"]["object"]

    if type(boxes) is list:
        for i in boxes:
            mask_status = i['name']
            
            x1 = int(i["bndbox"]["xmin"])
            y1 = int(i["bndbox"]["ymin"])
            x2 = int(i["bndbox"]["xmax"])
            y2 = int(i["bndbox"]["ymax"])
            features.append(img[y1:y2, x1:x2])
            labels.append(mask_status)
    else:
        mask_status = boxes['name']
        
        x1 = int(boxes["bndbox"]["xmin"])
        y1 = int(boxes["bndbox"]["ymin"])
        x2 = int(boxes["bndbox"]["xmax"])
        y2 = int(boxes["bndbox"]["ymax"])

        features.append(img[y1:y2, x1:x2])
        labels.append(mask_status)

list_of_pngs = []

for i in os.listdir("images"):
    list_of_pngs.append(i)

for i in list_of_pngs:
    create_train(i)

print('---------------Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

print("Length of images: ", len(list_of_pngs))
print("Length of features: ", len(features))
print("Length of labels: ", len(labels))

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

face_recognizer.sace('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
