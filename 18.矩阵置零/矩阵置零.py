#https://leetcode.cn/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：两次遍历。第一次遍历记录下出现0的行号和列号。第二次将出现0的行和列的元素都置为0.
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)#获取行数
        n=len(matrix[0])#获取列数
        col=set()#初始化哈希表用来存储出现0的列
        row=set()#初始化哈希表用来存储出现0的行
        #第一次遍历，记录下出现0的行号和列号
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        #第二次遍历，将出现0的行和列的元素都置为0
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j]=0
