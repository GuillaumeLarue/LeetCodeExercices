from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))


if __name__ == '__main__':
    def printTree(root: Optional[TreeNode]) -> None:
        if root is None:
            return
        print(root.val)
        printTree(root.left)
        printTree(root.right)

    so = Solution()
    tree = TreeNode(5,
                    TreeNode(4,
                             TreeNode(4, None,
                                      TreeNode(12,
                                               TreeNode(234, None, None),
                                               TreeNode(9, None, None))), None),
                    TreeNode(2, None, None))

    printTree(tree)
