
class Stack:

  def __init__(self):
    self.elements = []
  
  def push(self,element):
    self.elements.append(element)
  def size(self):
    cnt = 0
    for i in self.elements:
      cnt+=1
    return cnt
  
  def top(self):
    return self.elements[-1]

  def pop(self):
    return self.elements.pop()
  

stack = Stack()

stack.push(5)
stack.push(7)
stack.push(9)
print(stack.top())
stack.pop()
print(stack.pop())


