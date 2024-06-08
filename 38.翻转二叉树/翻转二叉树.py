#https://leetcode.cn/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用递归的方法，交换每个节点的左右子节点，即可生成二叉树的镜像

具体算法流程：

1. 终止条件：当节点root为空（也就是越过叶结点），则返回Null
2. 递推工作
   1. 初始化节点temp，用于暂存root的左子节点
   2. 开始递归右子节点，并将返回值作为root的左子节点
   3. 开启递归左子节点，并将返回值作为root的右子节点
3. 返回值：返回根节点root
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :return #终止条件：当节点root为空（也就是越过叶结点），则返回Null
        temp=root.left#初始化节点temp，用于暂存root的左子节点
        root.left=self.invertTree(root.right)#开始递归右子节点，并将返回值作为root的左子节点
        root.right=self.invertTree(temp)#开启递归左子节点，并将返回值作为root的右子节点
        return root#返回值：返回根节点root
