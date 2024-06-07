#https://leetcode.cn/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：采用层序遍历的方式，每层遍历结束即在结果上加一即可
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0#当树为空，返回0
        queue=[root]#先将根节点入队
        res=0#初始化结果为0
        #开始对队列中的元素进行遍历，每层遍历完成将结果+1
        while queue:
            for i in range(len(queue)):
                cur=queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res+=1
        return res#返回结果即可
