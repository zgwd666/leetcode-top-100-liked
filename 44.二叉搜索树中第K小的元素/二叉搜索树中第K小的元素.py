#https://leetcode.cn/problems/kth-smallest-element-in-a-bst/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
在二叉搜索树中，任意子节点都满足左子节点<根节点<右子节点的规则。因此二叉搜索树具有重要性质：二叉搜索树的中序遍历为递增序列。

也就是说，本题可被转化为求中序遍历第K个节点。

为了求第k个节点，需要实现以下三项工作：

1. 递归遍历时计数，统计当前节点的序号
2. 递归到第k个节点时，应记录结果res
3. 记录结果后，后序的遍历即失去意义，应提前返回。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root):#定义递归函数
            #当前结果为空或者已经遍历过目标节点直接返回
            if not root:return
            if self.k==0:return
        	#中序遍历 左->根->右
            helper(root.left)
            self.k-=1#目标值减一
            if self.k==0:self.res=root.val#判断是否为目标值
            helper(root.right)
        self.k=k#定义目标值
        helper(root)#进行递归
        return self.res#返回结果
