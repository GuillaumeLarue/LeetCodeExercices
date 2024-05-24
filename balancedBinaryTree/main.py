from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def rec(root: Optional[TreeNode]) -> (int, bool):
            if root is None:
                return 1, True
            h_left, a = rec(root.left)
            h_right, b = rec(root.right)
            if abs(h_left - h_right) > 1:
                return 0, False
            return 1 + max(h_left, h_right), a and b
        return rec(root)[1]


if __name__ == '__main__':
    so = Solution()

    tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, None,None), TreeNode(4, None,None)) , TreeNode(3, None, None)), TreeNode(2, None, None))
    print(so.isBalanced(tree))
