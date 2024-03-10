class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None 

def insert(root,x):
  if not root:
    return TreeNode(x)
  
  if  root.val< x: 
    root.right = insert(root.right,x)
  else:
    root.left = insert(root.left,x)
  return root

def minValue(root):
  cur = root
  while cur and cur.left:
    cur = cur.left
  return cur
  
def remove(root, x):
    # If the root is None (i.e., the tree is empty or we've reached an empty subtree), return None
    if not root:
        return None

    # If the value to be removed is greater than the root's value, go to the right subtree
    if root.val < x:
        root.right = remove(root.right, x)
    # If the value to be removed is less than the root's value, go to the left subtree
    elif root.val > x:
        root.left = remove(root.left, x)
    else:
        # We've found the node to be removed

        # Case 1: The node has no left child, so we just bypass this node and return its right child
        # This also covers the case where the node has no children at all, as root.right would be None
        if not root.left:
            return root.right
        # Case 2: The node has no right child, so we just bypass this node and return its left child
        elif not root.right:
            return root.left
        else:
            # Case 3: The node has two children

            # Find the minimum value in the right subtree
            minNode = minValue(root.right)
            # Replace the value of the node to be removed with the found minimum value
            root.val = minNode.val
            # Remove the node with the minimum value in the right subtree
            root.right = remove(root.right, minNode.val)

    # Return the new root of the subtree
    return root



# tree traversal O(n) -- DFS

def inorder(root): # Left,Root,Right
    if root:
        inorder(root.left)  # Visit left subtree
        print(root.val)              # Visit root node
        inorder(root.right) # Visit right subtree
def inorder_iterative(root):
    st = []
    cur = root
    while True:
        if cur is not None:
            st.append(cur)
            cur = cur.left
        elif(st):
            cur = st.pop()
            print(cur.val, end=" ")
            cur = cur.right
        else:
            break
    print()


def preorder(root): # Root, Left, Right
   if root:
      print(root.val)
      preorder(root.left)
      preorder(root.right)


def postorder(root): # Left, Right, Root 
   if root:
      postorder(root.left)
      postorder(root.right)
      print(root.val)

# tree traversal O(n)----> BFS
      
def bfs(root):
  queue = []
  if root:
    queue.append(root)
  
  lvl = 0 
  while len(queue)>0:
    print("level :",lvl)
    for i in range(len(queue)):
      cur = queue.pop(0)
      print(cur.val)
      if cur.left:
        queue.append(cur.left)
      if cur.right:
        queue.append(cur.right)
    lvl += 1



'''  
       4
      / \
     3   6
    /   / \
   2   5   7
'''
tr = TreeNode(4)

l = [3,2,6,5,7]
for i in l:
  insert(tr,i)

# remove(tr,4)
# inorder(tr.right)
bfs(tr)


  