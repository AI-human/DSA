class Pair:
  def __init__(self,key,val):
    self.key = key
    self.val = val
  
class HashMap:

  def __init__(self):
    self.size = 0
    self.capacity = 2
    self.map = [None,None]

  def hash(self,key):
    index = 0
    for k in key:
      index+=ord(k)
    return index%self.capacity
  
  def get(self,key):
    index = self.hash(key)
    while self.map[index]!=None:
      if self.map[index].key == key:
        return self.map[index].val
      index+=1
      index = index%self.capacity
    return None
  def put(self,key,val):
    index = self.hash(key)

    while True:
      if self.map[index]==None:
        self.map[index] = Pair(key,val)
        self.size+=1
        if self.size >= self.capacity//2:
          self.rehash()
          return
      elif self.map[index].key == key:
        self.map[index].val = val
        return
      
      index +=1
      index = index%self.capacity
        