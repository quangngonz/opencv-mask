import cv2 as cv
import json

img = cv.imread('./images/maksssksksss2.png')

with open("./jsons/maksssksksss2.xml.json") as json_file:
    data = json.load(json_file)

boxes = data["annotation"]["object"]

mask_statuses =['with_mask', 'without_mask', 'mask_weared_incorrect']
colors = [(0, 255, 0), (0, 0, 255), (0, 255, 255)]

for i in boxes:
    mask_status = i["name"]
    rect_color = colors[mask_statuses.index(mask_status)]
    
    x1 = int(i["bndbox"]["xmin"])
    y1 = int(i["bndbox"]["ymin"])
    x2 = int(i["bndbox"]["xmax"])
    y2 = int(i["bndbox"]["ymax"])
    cv.rectangle(img, (x1, y1), (x2, y2), rect_color, 2)

cv.imwrite('./processed_images/maksssksksss2.png', img)