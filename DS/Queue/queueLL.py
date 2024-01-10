class Node:
  def __init__(self,val):
    self.val = val
    self.next = None


class Queue:

  def __init__(self):
    self.begin=self.end = None
  
  def enqueue(self,val):
    new_node = Node(val)
    if self.begin==None and self.end==None:
      self.begin = new_node
      self.end = new_node
    else:
      self.end.next = new_node
      self.end = self.end.next

  def dequeue(self):
    if self.begin == None:
      print("queue empty nothing to dequeue")
      return -1
    self.begin = self.begin.next
    
      
  def traverse(self):
    cur = self.begin
    
    if cur==None:
      print("queue empty")
      return None
    while cur:
      print(cur.val)
      cur = cur.next


queue = Queue()

queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

# queue.traverse()