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
            # Check if the cell is surrounded by 2 layers of the same color
            if (grid[i-1][j] == color and grid[i+1][j] == color and
                grid[i][j-1] == color and grid[i][j+1] == color and
                grid[i-2][j] == color and grid[i+2][j] == color and
                grid[i][j-2] == color and grid[i][j+2] == color):
                # Append the index of the middle cell to the list
                middle_cells.append((i, j))
                skip=2;
    return middle_cells

# Example grid with 10 by 10 cells (0: black, 1: white)
grid = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

# Find all indices of middle cells surrounded by 2 layers of the same color
middle_cells = find_middle_cells_two_layers(grid)

if middle_cells:
    print("Indices of middle cells surrounded by 2 layers of the same color:")
    for cell in middle_cells:
        print(cell)
else:
    print("No middle cells surrounded by 2 layers of the same color found.")
