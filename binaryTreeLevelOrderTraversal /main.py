from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        seen = [False] * 3
        # FIXME

if __name__ == '__main__':
    so = Solution()

    tree = TreeNode(1,
                    TreeNode(2, TreeNode(3, TreeNode(4, None, None), TreeNode(4, None, None)), TreeNode(3, None, None)),
                    TreeNode(2, None, None))
    print(so.levelOrder(tree))
