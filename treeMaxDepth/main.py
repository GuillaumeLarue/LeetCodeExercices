from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def rec(root: Optional[TreeNode]):
            if root is None:
                return 0
            return 1 + max(rec(root.left), rec(root.right))
        return rec(root)

if __name__ == '__main__':
    so = Solution()
    tree = TreeNode(5, TreeNode(0, TreeNode(0, None, TreeNode(0, TreeNode(0, None, None), TreeNode(0, None, None))), None), TreeNode(2, None, None))

    print(so.maxDepth(tree))
