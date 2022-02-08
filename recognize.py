
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

mask_types = ['with_mask', 'without_mask', 'mask_weared_incorrect' ]

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('trained.yml')

img = cv.imread(r'./Samples/with_mask/maksssksksss26_0.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

label, confidence = face_recognizer.predict(gray)

print(f'Label = {mask_types[label]} with a confidence of {confidence}')

cv.imshow('Detected masks', img)

cv.waitKey(0)
