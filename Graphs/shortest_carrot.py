from collections import deque
def closest_carrot(grid, starting_row, starting_col):
  queue = deque([ (starting_row, starting_col, 0) ])
  visited = set([(starting_row, starting_col)])
  
  while queue:
    row, col, distance = queue.popleft()
    
    if grid[row][col] == 'C':
      return distance
    
    deltas = [(1,0),(-1,0),(0,1),(0,-1)]
    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = delta_row + row
      neighbor_col = delta_col + col
      pos = (neighbor_row,neighbor_col)
      
      row_inbounds = 0 <= neighbor_row < len(grid)
      col_inbounds = 0 <= neighbor_row < len(grid[0])
      if row_inbounds and col_inbounds and pos not in visited and grid[row][col] != 'X':
        queue.append((neighbor_row,neighbor_col,distance+1))
        visited.add(pos)
  return -1

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2)) # -> 4
    