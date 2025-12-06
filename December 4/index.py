# Read input from file
INPUT_FILE_NAME = "file.txt"   

def StarSeven():
    with open(INPUT_FILE_NAME, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    accessible_count = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '@':
                neighbor_count = 0
                
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if grid[new_row][new_col] == '@':
                            neighbor_count += 1
                
                if neighbor_count < 4:
                    accessible_count += 1
    
    print(f"Number of accessible paper rolls: {accessible_count}")



if __name__ == "__main__":
    StarSeven()
    