#https://leetcode.cn/problems/rotate-image/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：顺时针旋转90度，可以拆解为按照主对角线翻转，然后逐行进行倒序 
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)#获取数组的行数和列数
        #先按照矩阵的主对角线进行反转
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #对反转后的矩阵逐行进行倒序
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]
