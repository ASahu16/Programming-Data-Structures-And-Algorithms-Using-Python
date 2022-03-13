# A class to store a binary tree node
class Node:
    def __init__(self, key):
        self.key = key
 
 
# Recursive function to perform inorder traversal on a given binary tree
def inorder(root):
 
    if root is None:
        return
 
    inorder(root.left)
    print(root.key, end=' ')
    inorder(root.right)
 
 
# Recursive function to build a BST from a preorder sequence.
def constructBST(preorder, start, end):
 
    # base case
    if start > end:
        return None
 
    # Construct the root node of the subtree formed by keys of the
    # preorder sequence in range `[start, end]`
    node = Node(preorder[start])
 
    # search the index of the first element in the current range of preorder
    # sequence larger than the root node's value
    i = start
    while i <= end:
        if preorder[i] > node.key:
            break
        i = i + 1
 
    # recursively construct the left subtree
    node.left = constructBST(preorder, start + 1, i - 1)
 
    # recursively construct the right subtree
    node.right = constructBST(preorder, i, end)
 
    # return current node
    return node
 
 
if __name__ == '__main__':
 
    ''' Construct the following BST
              15
            /    \
           /      \
          10       20
         /  \     /  \
        /    \   /    \
       8     12 16    25
    '''
 
    preorder = [35, 23, 26, 46, 40, 39, 41, 52]
 
    # construct the BST
    root = constructBST(preorder, 0, len(preorder) - 1)
 
    # print the BST
    print('Inorder traversal of BST is ', end='')
 
    # inorder on the BST always returns a sorted sequence
    inorder(root)