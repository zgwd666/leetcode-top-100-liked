#https://leetcode.cn/problems/binary-tree-level-order-traversal/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：利用队列的性质，将每一层的节点从左到右入队，再从左到右出队
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []#空树，直接返回[]
        queue=[root]#跟节点入队
        res=[]#创建结果列表
        while queue:#进行遍历
            level=[]#创建列表存储本层的节点
            for i in range(len(queue)):#从左到右依次遍历本层的节点
                cur=queue.pop(0)#先将最左边的节点出队
                level.append(cur.val)#将其添加到本层列表中
                if cur.left:#存在左节点，左节点入队
                    queue.append(cur.left)
                if cur.right:#存在右节点，右节点入队
                    queue.append(cur.right)
            res.append(level)#将本层的结果添加到最终结果中
        return res#返回结果列表
