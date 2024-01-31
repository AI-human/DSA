class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList():
  prev, cur = None,head
  while cur:
      temp_next = cur.next # initialize a temporary var
      cur.next = prev
      prev = cur
      cur = temp_next
  return prev # head node
