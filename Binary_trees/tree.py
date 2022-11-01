class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def DFS(root):
    if root is None:
        return []
    stack = [root]
    values = []
    
    while stack:
        current = stack.pop()
        if current.left is None and current.right is None:
            values.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return values