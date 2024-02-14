class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None 

def insert(root,x):
  if not root:
    return TreeNode(x)
  
  elif  root.val< x: 
    root.right = insert(root.right,x)
  elif root.val> x:
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



def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)  # Visit left subtree
        print(root.val)              # Visit root node
        inorder_traversal(root.right) # Visit right subtree





'''  
       4
      / \
     3   6
    /   / \
   2   5   7
'''
tr = TreeNode(4)

l = [2,3,6,5,7]
for i in l:
  insert(tr,i)

remove(tr,4)
inorder_traversal(tr)


    