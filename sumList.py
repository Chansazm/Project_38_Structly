class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def sum_list(head):
  sum = 0
  current = head
  while head is not None:
    sum += current.val
    current = current.next
  return sum

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')