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
        skip=0;
        for j in range(2, cols - 2):
            color = grid[i][j]
            if(color==0 or skip > 0):
                skip-=1
                continue;
            print(grid[i][j])
            # Check if the cell is surrounded by 2 layers of the same color
            if (grid[i-1][j] == color and grid[i+1][j] == color and
                grid[i][j-1] == color and grid[i][j+1] == color and
                grid[i-2][j] == color and grid[i+2][j] == color and
                grid[i][j-2] == color and grid[i][j+2] == color):
                # Append the index of the middle cell to the list
                middle_cells.append((i, j))
                skip=2;
    return middle_cells

# Read the image
image = cv2.imread('grid.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to obtain white regions
_, white_mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Define the grid size
grid_size = 200
# Overlay grid lines on the original image
rows, cols = gray.shape

# Draw horizontal lines
for i in range(0, rows, grid_size):
    cv2.line(image, (0, i), (cols, i), (0, 255, 0), 1)

# Draw vertical lines
for j in range(0, cols, grid_size):
    cv2.line(image, (j, 0), (j, rows), (0, 255, 0), 1)

whites = [[0] * cols for _ in range(rows)]
for i in range(0, rows, grid_size):
    for j in range(0, cols, grid_size):
        # Extract the cell's region
        cell = white_mask[i:i+grid_size, j:j+grid_size]
        # Check if at least 50% of the cell is white
        if np.mean(cell) >= 50:  # Assuming white has intensity > 127.5 for 50%
            # Highlight the cell
            whites[i][j]=1
            cv2.rectangle(image, (j, i), (j+grid_size, i+grid_size), (0, 0, 255), 1)
print(find_middle_cells_two_layers(whites))
# Display the image with highlighted cells
# print(whites)            
cv2.imshow('Image with Highlighted Cells', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
