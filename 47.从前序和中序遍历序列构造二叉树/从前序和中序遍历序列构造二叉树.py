#https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
先序遍历的顺序为中->左->右

中序遍历的顺序为左->中->右

可以将先序遍历中第一个元素取出，作为根节点的值，在中序遍历数组中寻找该值的位置，该位置之前的数组元素全为左子树的值；该位置之后的数组元素全为右子树的值。且先序遍历的左子树和中序遍历的左子树的数组的长度一致，将先序遍历的左子树数组和右子树数组就也可以切分出来，一直递归，直到碰到None为止。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:return#递归终止条件，当没有节点，返回
        val=preorder[0]#取出先序遍历数组的第一个元素也就是根节点的值
        root=TreeNode(val)#创建根节点
        index=inorder.index(val)#寻找根节点在中序遍历中的位置
        #根据位置将中序遍历数组划分为左中序遍历数组和中先序遍历数组
        leftInorder=inorder[:index]
        rightInorder=inorder[index+1:]
        #根据中序遍历左右数组的长度将先序遍历数组也划分为左先序遍历数组和先先序遍历数组
        leftPreorder=preorder[1:index+1]
        rightPreorder=preorder[index+1:]
        #递归计算左子树和右子树
        root.left=self.buildTree(leftPreorder,leftInorder)
        root.right=self.buildTree(rightPreorder,rightInorder)
        return root#返回根节点
