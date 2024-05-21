from treeMaxDepth.main import Solution, TreeNode


class TestInvertBinaryTree:

    def test_one(self):
        so = Solution()
        tree = TreeNode(5, TreeNode(0, None, None), TreeNode(2, None, None))
        assert so.maxDepth(tree) == 2

    def test_two(self):
        so = Solution()
        tree = TreeNode(5, TreeNode(0, TreeNode(0, None, TreeNode(0, TreeNode(0, None, None), TreeNode(0, None, None))), None), TreeNode(2, None, None))
        assert so.maxDepth(tree) == 5