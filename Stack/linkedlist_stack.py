class Node:
  def __init__(self,val):
    self.val = val 
    self.next = None

class Stack:

  def __init__(self):
    self.top = Node(0)
  
  def push(self,x):
    new_node = Node(x)
    new_node.next = self.top
    self.top = new_node 

  def pop(self):
    if (self.top.val==0):
      print("underflow")
    self.top = self.top.next
  
  def Top(self):
    return self.top.val

  def traverse(self):
    cur = self.top
    while cur:
      if (self.top.val==0):
        print("underflow")
        break
      print(cur.val)
      cur=cur.next


stck = Stack()

stck.push(1)
stck.push(2)
stck.push(3)
# print(stck.Top())
stck.pop()
stck.pop()
# stck.pop()
# stck.pop()
print(stck.traverse())
