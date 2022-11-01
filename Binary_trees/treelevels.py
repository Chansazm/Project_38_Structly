class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def tree_levels(root):
    if root is None:
        return []
    levels = []
    queue = [(root,0)]
    
    while queue:
        node, level_num = queue.pop(0)
        if len(levels) == level_num:
            levels.append([node.val])
        else:
            levels[level_num].append(node.val)
        
        if node.left:
            queue.append((node.left,level_num + 1))
        if node.right:
            queue.append((node.right,level_num + 1))
            
    print(levels)
    



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]