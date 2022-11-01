class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def tree_levels(root):
    levels = []
    _fill_levels(root,levels,0)
    print(levels)

def _fill_levels(root,levels, level_num):
    if root is None:
        return []
    if len(levels) == level_num:
        levels.append([root.val])
    else:
        levels[level_num].append(root.val)
    _fill_levels(root.left,levels,level_num + 1)
    _fill_levels(root.right,levels,level_num + 1)
    
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
    