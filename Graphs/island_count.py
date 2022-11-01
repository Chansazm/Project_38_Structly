def island_count(grid):
  visited = set()
  count = 0
  for r in range(len(grid)):#row
    for c in range(len(grid[0])):#column
      if explore(grid,r,c,visited) == True:
        count += 1
  return count

def explore(grid,r,c,visited):
  #Check inbounds
  row_inbound = 0 <= r < len(grid)
  col_inbound = 0<= c < len(grid[0])
  if not row_inbound or not col_inbound:
    return False
  #check if water
  if grid[r][c] == 'W':
    return False
  #check visited
  pos = r,c
  if pos in visited:
    return False
  visited.add(pos)
  
  explore(grid,r-1,c,visited)
  explore(grid,r+1,c,visited)
  explore(grid,r,c-1,visited)
  explore(grid,r,c+1,visited)
  
  return True