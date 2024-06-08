#https://leetcode.cn/problems/symmetric-tree/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路
对称二叉树的每一层的节点都应该是对称的，所以我们就可以采用广度优先遍历，对每一层进行遍历，并对每一层的遍历数组结果检查是否为对称数组。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left:#只有一个节点，那么就是对称的
            return True
        queue=[root]#根节点入队
        while queue:#进行遍历
            level=[]#初始化结果数组用来存储本层的节点
            for i in range(len(queue)):#对本层的每一个节点进行遍历
                cur=queue.pop(0)#出队
                if cur:#如果当前节点不为空
                    level.append(cur.val)#将节点值加入到结果中
                    queue.append(cur.left)#将左右子节点加入队列
                    queue.append(cur.right)
                else:#如果当前的节点为空
                    level.append(None)#结果链表中直接添加None
            if level!=level[::-1]:return False#如果当前层的节点数值不是对称，直接返回false
        return True#遍历完成且每层都是对称的，返回True
