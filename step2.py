import cv2
import numpy as np

def find_middle_cells_two_layers(grid):
          # Define the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # List to store indices of middle cells
    middle_cells = []
    
    # Iterate over each cell in the grid
    for i in range(2, rows - 2):
        for j in range(2, cols - 2):
            color = grid[i][j]
            if color == 0:
              continue
            
            # Check if the cell is surrounded by 2 layers of the same color
            if (grid[i-1][j] == color and grid[i+1][j] == color and
                grid[i][j-1] == color and grid[i][j+1] == color and
                grid[i-2][j] == color and grid[i+2][j] == color and
                grid[i][j-2] == color and grid[i][j+2] == color):
                # Append the index of the middle cell to the list
                middle_cells.append((i, j))
    
    return middle_cells

# Read the image
image = cv2.imread('grid.jpg')

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
        for j in range(0, cols, grid_size):
            cell = resized_contour_region[i:i+grid_size, j:j+grid_size]
            if np.mean(cell) > 200:  # Assuming white has intensity > 200
                cv2.rectangle(resized_contour_region, (j, i), (j+grid_size, i+grid_size), (0, 0, 255), 1)

    # Display the resized contour region with highlighted white cells
    cv2.imshow('Resized Contour Region with Highlighted White Cells', resized_contour_region)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No white segments found.")
