class TreeNode: 
    def __init__(self,val): 
        self.left = None
        self.right = None
        self.val = val 
        
# A utility function to insert a new node with the given key 
def insert(self, val): 
    if self is None:
        self= val
    else:
        if val < self.val: 
            if self.left is None: 
                self.left = TreeNode(val) 
            else: 
                self.left.insert(val) 
        else: 
            if self.right is None: 
                self.right = TreeNode(val) 
            else: 
                self.right.insert(val)

#def inorder_traversal(self):
 #   if self.left:
#        self.left.inorder_traversal()
    print(self.value)
    if self.right:
         self.right.inorder_traversal()

def preorder_traversal(self):
    if self.left:
          self.left.inorder_traversal()
    print(self.value)
    if self.right:
         self.right.inorder_traversal()


tree =TreeNode(6)
tree.insert(2)


TreeNode.inorder_traversal()
