# import json
# path = "./label-studio/annotations/result.json"
# f = open(path)
# anns = json.load(f)
# print(anns.keys())
from pycocotools.coco import COCO
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

ann_file = "./label-studio/annotations/result.json"
coco=COCO(ann_file)
 
# Get list of category_ids, here [2] for bicycle
category_ids = coco.getCatIds(['grated'])


# Get list of image_ids which contain bicycles
image_ids = coco.getImgIds(catIds=[0])
print(image_ids[0:5])

# image = Image.open("./IMG_5661.jpg")
# image = Image.open("./coconuts/IMG_5661.jpeg")
image = Image.open("./coconuts/IMG_5661.jpeg")

annotation_ids = coco.getAnnIds(imgIds=0, catIds=[0])
anns = coco.loadAnns(annotation_ids)


fig, ax = plt.subplots()
for ann in anns:
    box = ann['bbox']
    bb = patches.Rectangle((box[0],box[1]), box[2],box[3], linewidth=2, edgecolor="blue", facecolor="none")
    ax.add_patch(bb)
 
ax.imshow(image)
plt.show()
