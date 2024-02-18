import cv2
import numpy as np

# Read the image
image = cv2.imread("./coconuts/23.jpeg")

# Convert BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range for white color in HSV
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 30, 255])

# Create a mask for white color
mask = cv2.inRange(hsv_image, lower_white, upper_white)

# Apply the mask to the original image
white_regions = cv2.bitwise_and(image, image, mask=mask)

# Display the original image and the white regions
cv2.imshow('Original Image', image)
cv2.imshow('White Regions', white_regions)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# import numpy as np

# # Read the image
# image = cv2.imread("./coconuts/23.jpeg")

# # Convert BGR to HSV
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# # Define range for white color in HSV
# lower_white = np.array([0, 0, 200])
# upper_white = np.array([180, 30, 255])

# # Create a mask for white color
# mask = cv2.inRange(hsv_image, lower_white, upper_white)

# # Find contours in the mask
# contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Draw polygons around the detected contours
# for contour in contours:
#     perimeter = cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
#     cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

# # Display the original image with polygons around white regions
# cv2.imshow('Contours around White Regions', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
