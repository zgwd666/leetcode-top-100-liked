#https://leetcode.cn/problems/search-a-2d-matrix-ii/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
本题可以借助矩阵的右上角元素进行范围的有效缩减。

如果当前矩阵的右上角小于target，证明第一行的所有元素都小，直接舍弃第一行，将对比点来到第二行最后一列。

如果当前矩阵的右上角大于target，证明最后一列的所有元素都大，直接舍弃最后一列，将对比点来到第一行倒数第二列。

一直缩减直到找到target或者跳出矩阵范围为止。
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])#获取矩阵的行数和列数
        row,col=0,n-1#初始点定位到矩阵的右上角
        while row<m and col>=0:#如果当前的点仍然在矩阵范围内，继续遍历
            if matrix[row][col]==target:#找到target，返回true
                return True
            elif matrix[row][col]>target:#如果当前矩阵的右上角大于target，证明最后一列的所有元素都大，直接舍弃最后一列，将对比点来到第一行倒数第二列。
                col-=1
            else:#如果当前矩阵的右上角小于target，证明第一行的所有元素都小，直接舍弃第一行，将对比点来到第二行最后一列。
                row+=1
        return False#超过矩阵的范围仍然没有找到目标值，返回Fasle
