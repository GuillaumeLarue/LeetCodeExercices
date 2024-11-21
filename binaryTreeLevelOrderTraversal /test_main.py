from binaryTreeLevelOrderTraversal.main import Solution, TreeNode


class TestInvertBinaryTree:
    # FIXME
    def test_one(self):
        so = Solution()
        tree = tree = TreeNode(5,
                    TreeNode(0, TreeNode(0, None, TreeNode(0, TreeNode(0, None, None), TreeNode(0, None, None))), None),
                    TreeNode(2, None, None))
        assert not so.levelOrder(tree)

    def test_two(self):
        so = Solution()
        tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, None, None), TreeNode(4, None, None)),
                                    TreeNode(3, None, None)), TreeNode(2, None, None))
        assert not so.levelOrder(tree)