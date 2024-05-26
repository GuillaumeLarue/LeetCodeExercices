from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def rec(root: Optional[TreeNode]) -> (int, int):
            if root is None:
                return 0, 0
            max_h_left, a = rec(root.left)
            max_h_right, b = rec(root.right)

            return 1 + max(max_h_left, max_h_right), max(max_h_left + max_h_right, max(a, b))

        return rec(root)[1]

    def printTree(self, root: Optional[TreeNode]) -> None:
        if root is None:
            print("None")
        else:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)


if __name__ == '__main__':
    so = Solution()
    tree = TreeNode(1,
                    TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)),
                    TreeNode(3, None, None))
    print(so.diameterOfBinaryTree(tree))
