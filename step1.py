import cv2
import numpy as np

# Read the image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to obtain white regions
_, white_mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Find contours in the white mask
contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour with the largest area
if contours:
    biggest_contour = max(contours, key=cv2.contourArea)

    # Create a mask for the contour region
    contour_mask = np.zeros_like(gray)
    cv2.drawContours(contour_mask, [biggest_contour], -1, (255), thickness=cv2.FILLED)

    # Find the minimum enclosing rectangle (bounding box) of the contour
    x, y, w, h = cv2.boundingRect(biggest_contour)

    # Apply the mask to the original image
    contour_region = cv2.bitwise_and(image, image, mask=contour_mask)

    # Crop the contour region from the original image
    contour_region = contour_region[y:y+h, x:x+w]

    # Resize the contour region image to fit the contour
    resized_contour_region = cv2.resize(contour_region, (w, h))

    # Overlay grid lines on the resized contour region
    grid_size = 100
    rows, cols, _ = resized_contour_region.shape
    for i in range(0, rows, grid_size):
        cv2.line(resized_contour_region, (0, i), (cols, i), (0, 255, 0), 1)
    for j in range(0, cols, grid_size):
        cv2.line(resized_contour_region, (j, 0), (j, rows), (0, 255, 0), 1)

    # Display the resized contour region with grid lines
    cv2.imshow('Resized Contour Region with Grid', resized_contour_region)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No white segments found.")
