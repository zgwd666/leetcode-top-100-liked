#https://leetcode.cn/problems/climbing-stairs/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用动态规划解题

1.确定dp数组以及下标的含义：

dp[i]:爬上第i阶台阶共有n中方法

2.确定递推公式

dp[i]=dp[i-1]+dp[i-2]

3.初始化dp数组

dp[1]=1 dp[2]=2

4.确定遍历顺序

从前向后遍历
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:return n#当n小于3，那就几级台阶就有几种方法 
        dp=[0]*(n+1)#创建dp数组
        #dp数组初始化
        dp[1]=1
        dp[2]=2
        #进行遍历
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]#根据递推公式计算
        return dp[-1]#返回最终结果
