#https://leetcode.cn/problems/pascals-triangle/description/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用动态规划的解法

1.确定dp数组以及下标的含义

$$dp[i][j]是在第i行第j列位置的值$$

2.确定递推公式

根据杨辉三角的规律，易得$$dp[i][j]=dp[i-1][j-1]+dp[i-1][j]$$

3.初始化

全部初始化为0即可

4.确定遍历顺序

从前向后，从上到下
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #当行数小于三，无法使用递推公式，直接返回值就可以
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        dp=[[1 for i in range(t)]for t in range(1,numRows+1)]#创建并初始化状态转移数组
        #进行遍历
        for i in range(2,numRows):
            for j in range(1,len(dp[i])-1):
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]#根据递推公式计算
        return dp#返回结果数组
