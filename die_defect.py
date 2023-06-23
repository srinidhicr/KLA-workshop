import json 
import numpy as np
from PIL import Image
import cv2

with open("input.json") as file:
    contents = file.read()

values = json.loads(contents)

#co-ordinates of region of interest
x1 = values['care_areas'][0]["top_left"]["x"]
y1 = values['care_areas'][0]["top_left"]["y"]
x2 = values['care_areas'][0]["bottom_right"]["x"]
y2 = values['care_areas'][0]["bottom_right"]["y"]

#size of the given image
img = Image.open("wafer_image_1.png")
width, height = img.width, img.height

"""img1 = cv2.imread(r'wafer_image_1.png', 0)
img2 = cv2.imread(r'wafer_image_2.png', 0)
sub = cv2.subtract(img1, img2)

coords = np.argwhere(sub > 0)
coords[:10]
coords_list = coords.tolist()
print(coords_list)"""

# data contains all differences between w1-w2 && w1-w3 && w1-w4 && w1-w5
coord_lists = {}  
img1 = cv2.imread(r'wafer_image_1.png', 0)
for i in range(2, 6):
    img2 = cv2.imread(r'wafer_image_'+ str(i) +'.png', 0)
    sub = cv2.subtract(img1, img2)
    data = []
    coords = np.argwhere(sub > 0)
    coords_list = coords.tolist()
    data.append(coords_list)
    coord_lists['new{}'.format(i + 1)] = data

"""for key, value in coord_lists.items():
    print(key, value)
"""

    
  




