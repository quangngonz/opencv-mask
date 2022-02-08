import cv2 as cv
import json, os

def write_image(img ,imagefile, x1, y1, x2, y2, mask_status):
    if mask_status == 'with_mask':
        cv.imwrite('./positive/' + imagefile, img[y1:y2, x1:x2])
    elif mask_status == 'without_mask':
        cv.imwrite('./negative/' + imagefile, img[y1:y2, x1:x2])
    else:
        cv.imwrite('./medium/' + imagefile, img[y1:y2, x1:x2])

def draw(imagefile):
    img = cv.imread('./images/'+ imagefile)
    print(imagefile)
    
    jsonFileName = imagefile.split('.')[0] + '.xml.json'
    with open("./jsons/" + jsonFileName) as json_file:
        data = json.load(json_file)

    boxes = data["annotation"]["object"]

    colors = {
        'with_mask': (0, 255, 0),
        'without_mask': (0, 0, 255),
        'mask_weared_incorrect': (0, 255, 255)
    }

    mask_statuses = ['with_mask', 'without_mask', 'mask_weared_incorrect']

    if type(boxes) is list:
        for i in boxes:
            mask_status = i['name']

            if mask_status in mask_statuses:
                rect_color = colors[mask_status]
            else:
                rect_color = (0, 0, 0)
            
            x1 = int(i["bndbox"]["xmin"])
            y1 = int(i["bndbox"]["ymin"])
            x2 = int(i["bndbox"]["xmax"])
            y2 = int(i["bndbox"]["ymax"])

            size = len(imagefile)

            print(imagefile[:size-4] + "_"+ str(boxes.index(i)) + ".png : " + mask_status)

            write_image(img, imagefile[:size-4] + "_"+ str(boxes.index(i)) + ".png", x1, y1, x2, y2, mask_status)

            cv.rectangle(img, (x1, y1), (x2, y2), rect_color, 2)
    else:
        mask_status = boxes['name']

        if mask_status in mask_statuses:
            rect_color = colors[mask_status]
        else:
            rect_color = (0, 0, 0)
        
        x1 = int(boxes["bndbox"]["xmin"])
        y1 = int(boxes["bndbox"]["ymin"])
        x2 = int(boxes["bndbox"]["xmax"])
        y2 = int(boxes["bndbox"]["ymax"])

        size = len(imagefile)

        print(imagefile[:size-4] + "_"+ "0" + ".png : " + mask_status)

        write_image(img, imagefile[:size-4] + "_"+ "0" + ".png", x1, y1, x2, y2, mask_status)

        cv.rectangle(img, (x1, y1), (x2, y2), rect_color, 2)

    size = len(imagefile)
    ouput_name = './processed_images/' + imagefile[:size-4] + '_processed.png'
    cv.imwrite(ouput_name, img)

list_of_jsons = []
list_of_pngs = []

for i in os.listdir("jsons"):
    list_of_jsons.append(i)

for i in os.listdir("images"):
    list_of_pngs.append(i)

for i in list_of_pngs:
    if i.split('.')[0] + '.xml.json' in list_of_jsons:
        draw(i)
    else:
        print('Json Not found for: ' + i)