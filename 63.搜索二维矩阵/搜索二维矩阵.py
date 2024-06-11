#https://leetcode.cn/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用排除法。

矩阵的右上角为本行的最大值和本列的最小值。所以每次对矩阵的右上角的值进行判断，如果右上角的值等于目标值，直接返回True；如果右上角的值小于目标值，则证明本行的所有值都小于目标值，将本行进行排除，重新定位到新的矩阵的右上角进行判断；如果右上角的值大于目标目标值，则证明本列的所有值都大于目标值，将本列排除，重新定位到矩阵的右上角进行判断。

如果遍历结果仍然没有找到目标值，就返回False
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])#获取矩阵的行列数
        row,col=0,n-1#定位到初始的右上角的位置
        while row<m and col>=0:#当前右上角的点位处于矩阵内才能遍历
            if matrix[row][col]==target:#如果右上角的值等于目标值，直接返回True
                return True
            elif matrix[row][col]<target:#如果右上角的值小于目标值，则证明本行的所有值都小于目标值，将本行进行排除，重新定位到新的矩阵的右上角进行判断
                row+=1
            else:#如果右上角的值大于目标目标值，则证明本列的所有值都大于目标值，将本列排除，重新定位到矩阵的右上角进行判断。
                col-=1
        return False#如果遍历结果仍然没有找到目标值，就返回False
