import cv2

# Load the image
image = cv2.imread('image.jpg')

# Assuming 'detection' contains the coordinates of the detected object
detection_x, detection_y, detection_w, detection_h = detection

# Calculate the center coordinates of the detection
detection_center_x = detection_x + detection_w / 2
detection_center_y = detection_y + detection_h / 2

# Calculate the center coordinates of the image
image_center_x = image.shape[1] / 2
image_center_y = image.shape[0] / 2

# Calculate the distance between the centers
distance = ((detection_center_x - image_center_x) ** 2 + (detection_center_y - image_center_y) ** 2) ** 0.5

print("Distance from center of the image to the detection:", distance)
