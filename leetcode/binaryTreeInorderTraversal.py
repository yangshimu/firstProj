# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        output = []
        self.recurHelp(root, output)
        return output

    def recurHelp(self, root, output):
        if root is None:
            return
        else:
            self.recurHelp(root.left, output)
            output.append(root.val)
            self.recurHelp(root.right, output)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3

sot = Solution()
out=sot.inorderTraversal(node1)
print(out)