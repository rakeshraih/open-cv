
import cv2 
import numpy as np 
from IPython.display import Image, display 
from matplotlib import pyplot as plt

#https://www.geeksforgeeks.org/image-segmentation-with-watershed-algorithm-opencv-python/
# Plot the image 
def imshow(img, ax=None): 
    if ax is None: 
        ret, encoded = cv2.imencode(".jpg", img) 
        print(encoded)
        # Convert the encoded image data to bytes
        encoded_bytes = encoded.tobytes()

        # Display the image using IPython.display
        display(Image(data=encoded_bytes))
        #display(Image(encoded)) 
    else: 
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) 
        ax.axis('off') 
  
#Image loading 
img = cv2.imread("./coconuts/1.jpeg") 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
#Threshold Processing 
ret, bin_img = cv2.threshold(gray, 
                             0, 255,  
                             cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) 


# noise removal 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)) 
bin_img = cv2.morphologyEx(bin_img,  
                           cv2.MORPH_OPEN, 
                           kernel, 
                           iterations=2) 

# Create subplots with 1 row and 2 columns 
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8)) 
# sure background area 
sure_bg = cv2.dilate(bin_img, kernel, iterations=3) 
imshow(sure_bg, axes[0,0]) 
axes[0, 0].set_title('Sure Background') 
  
# Distance transform 
dist = cv2.distanceTransform(bin_img, cv2.DIST_L2, 5) 
imshow(dist, axes[0,1]) 
axes[0, 1].set_title('Distance Transform') 
  
#foreground area 
ret, sure_fg = cv2.threshold(dist, 0.5 * dist.max(), 255, cv2.THRESH_BINARY) 
sure_fg = sure_fg.astype(np.uint8)   
imshow(sure_fg, axes[1,0]) 
axes[1, 0].set_title('Sure Foreground') 
  
# unknown area 
unknown = cv2.subtract(sure_bg, sure_fg) 
imshow(unknown, axes[1,1]) 
axes[1, 1].set_title('Unknown') 
  

# Marker labelling 
# sure foreground  
ret, markers = cv2.connectedComponents(sure_fg) 
  
# Add one to all labels so that background is not 0, but 1 
markers += 1
# mark the region of unknown with zero 
markers[unknown == 255] = 0
  
fig, ax = plt.subplots(figsize=(6, 6)) 
ax.imshow(markers, cmap="tab20b") 
ax.axis('off') 
plt.show()


# cv2.imshow('Image', bin_img)
# # Wait for any key press
# cv2.waitKey(0)

# # Close all OpenCV windows
# cv2.destroyAllWindows()