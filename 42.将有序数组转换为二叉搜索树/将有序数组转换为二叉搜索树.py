#https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
二叉搜索树的定义是左节点的值小于根节点的值小于右节点的值，且需要平衡。那么就可以将升序数组的中间节点作为平衡搜索树的根节点，前半数组作为左子树，后半节点作为右子树，一直递归，直到数组为空。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:return None#当数组为空，返回None
        l,r=0,len(nums)-1#获取数组的左右位置
        mid=(l+r)//2#计算中间位置
        root=TreeNode(nums[mid])#将中间位置作为父节点
        root.left=self.sortedArrayToBST(nums[:mid])#将前半数组作为左子树进行递归
        root.right=self.sortedArrayToBST(nums[mid+1:])#将后半数组作为右子树进行递归
        return root#返回根节点
