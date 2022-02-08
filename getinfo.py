import os

from matplotlib import image

mask_types = ['with_mask', 'without_mask', 'mask_weared_incorrect' ]
DIR = r'./Samples'

images = 0

path = os.path.join(DIR, 'with_mask')
print(path)
for img in os.listdir(path):
    images += 1

print('Total images with mask: ', images)

images = 0

path = os.path.join(DIR, 'without_mask')
print(path)
for img in os.listdir(path):
    images += 1

print('Total images without mask: ', images)

images = 0

path = os.path.join(DIR, 'mask_weared_incorrect')
print(path)
for img in os.listdir(path):
    images += 1

print('Total images with mask weared incorrectly: ', images)
