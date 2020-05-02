class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        if not root.left and not root.right:
            return root.val
        length, ans = self.helper(root)
        return ans

    def helper(self, subroot):
        if not subroot: return 0, 0
        if not subroot.left and not subroot.right:
            return subroot.val, subroot.val
        leftLen, leftPath = self.helper(subroot.left)
        rightLen, rightPath = self.helper(subroot.right)
        Len = Path = subroot.val
        if leftLen < 0: leftLen = 0
        if rightLen < 0: rightLen = 0
        Path += leftLen + rightLen
        if leftLen >= rightLen:
            Len += leftLen
        else:
            Len += rightLen
        maxPath = max(Path, leftPath, rightPath)
        return Len, maxPath


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3

sot =Solution()
print(sot.maxPathSum(node1))