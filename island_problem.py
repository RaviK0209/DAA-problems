def numIslands(grid):
    
    if not grid:
        return 0

    def dfs(grid, i, j):
        # Check the boundaries of the grid and whether the current cell is '1' (land)
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return

        # Mark the current cell as visited by setting it to '0'
        grid[i][j] = '0'

        
        dfs(grid, i+1, j)  # Down
        dfs(grid, i-1, j)  # Up
        dfs(grid, i, j+1)  # Right
        dfs(grid, i, j-1)  # Left

   
    island_count = 0

    
    for i in range(len(grid)):# row
        for j in range(len(grid[0])):#col in each row
            # If the current cell is '1', it's part of an island
            if grid[i][j] == '1':
                # Start a DFS to mark the entire island as visited
                dfs(grid, i, j)
               
                island_count += 1

    return island_count


grid = [
    ['1', '1', '0', '1', '0'],
    ['0', '1', '1', '0', '1'],
    ['1', '0', '1', '1', '1'],
    ['0', '0', '1', '0', '0']
]


print(f"maximum no. of island are:- {numIslands(grid)}")