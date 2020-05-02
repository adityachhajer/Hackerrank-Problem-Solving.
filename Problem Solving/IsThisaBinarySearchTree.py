""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if (root.left is None) and (root.right is None):
        return True
    elif(root.left is None) and (root.right is not None):
        if(root.right.info>root):
            check_binary_search_tree_(root.right)
        else:
            return False
    elif (root.left is not None) and (root.right is  None):
        if (root.left.info < root):
            check_binary_search_tree_(root.left)
        else:
            return False
    elif((root.left.info==root.info) or (root.right.info==root.info)):
        return False

    else:
        if(root.left.data<root.data and root.right.data>root.data):
            check_binary_search_tree_(root.left)
            check_binary_search_tree_(root.right)
        else:
            return False
