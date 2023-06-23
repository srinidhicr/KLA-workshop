import json 
from PIL import Image

with open("input.json") as file:
    contents = file.read()

values = json.loads(contents)
left = values["care_areas"]
print(left)
img = Image.open("wafer_image_1.png")
#im.show()
care_area = img.crop()
