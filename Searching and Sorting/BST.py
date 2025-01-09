class TreeNode:
    def __init__(self,val):
        self.root = val
        self.left = None
        self.right = None
    def Insert(root,val):
        #case1:
        if not root:
            return TreeNode(val)
        elif root.val == val:
            return root
        elif val < root.val:
            return root.left = Insert(root.left,val)
        else:
            return  root.right = Insert(root.right,val)
        return root
    def inorder(root):
        if root:
            inorder(root.left)
            print(root.val)
            inorder(root.right)
r = TreeNode(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

