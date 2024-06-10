#https://leetcode.cn/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
本题实际上要求每层的最右侧的一个节点。也就对应层序遍历的每一层的最后一个值。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []#空树直接返回[]
        queue=[root]#根节点入队
        res=[]#创建结果列表
        while queue:#对队列进行遍历
            level=[]#初始化本层节点值结果列表
            for i in range(len(queue)):#对本层的每一个节点进行遍历
                cur=queue.pop(0)#出队
                level.append(cur.val)#将结果添加到本层结果列表中
                if cur.left:#存在左子节点，左子节点入队
                    queue.append(cur.left)
                if cur.right:#存在右子节点，右子节点入队
                    queue.append(cur.right)
            res.append(level[-1])#将本层最靠右的节点加入结果中
        return res#返回结果
