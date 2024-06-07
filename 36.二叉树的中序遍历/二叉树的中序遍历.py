#https://leetcode.cn/problems/binary-tree-inorder-traversal/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：中序遍历的顺序时左节点->父节点->右节点，采用递归的方式实现以上的顺序即可
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]#创建结果数组
        def helper(root):#定义中序遍历递归函数
            if not root:return#当前节点为空返回
            helper(root.left)#先遍历左子节点
            res.append(root.val)#加入当前节点的值
            helper(root.right)#最后遍历右子节点
        helper(root)#进行中序遍历
        return res#返回结果
