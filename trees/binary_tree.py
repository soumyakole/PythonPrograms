class BinaryTreeNode:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item
    def is_leaf(self):
        return self.left is None and self.right is None
    def __str__(self):
        return "BinaryTreeNode [item=%s, left=%s, right=%s]" %(self.item, self.left, self.right)


if __name__=='__main__':
    bn1 = BinaryTreeNode(1)
    print(bn1)