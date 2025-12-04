
DXY = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

with open('input', 'r') as file:
    grid = [[x for x in line.strip()] for line in file.readlines()]
    h = len(grid)
    w = len(grid[0])
    removed = 0

    while True:
        accessible = 0
        for x in range(w):
            for y in range(h):
                if grid[y][x] == '@':
                    occuppied_neighbors = 0
                    for dx, dy in DXY:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] in ('@', 'x'):
                            occuppied_neighbors += 1
                            if occuppied_neighbors >= 4:
                                break
                    if occuppied_neighbors < 4:
                        accessible += 1
                        grid[y][x] = 'x'
        if accessible == 0:
            break  # Done
        removed += accessible
        # Clean up for next iteration
        for x in range(w):
            for y in range(h):
                if grid[y][x] == 'x':
                    grid[y][x] = '.'

    # Print completed grid for visualization
    for line in grid:
        print(''.join(line))
    print(removed)
