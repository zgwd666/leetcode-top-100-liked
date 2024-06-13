#https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用动态规划解题。

1.确定dp数组以及下标的含义

dp[i]:第i天能获得的最大利润

2.递推公式

$$dp[i]=max(dp[i-1],price[i]-minPrice)$$

3.初始化

dp[0]=0

minPrice初始化为price[0]

4.确定遍历顺序

从前向后遍历
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[0]*len(prices)#创建状态转移数组
        minPrice=prices[0]#初始化最小成
        for i in range(1,len(prices)):#进行遍历
            minPrice=min(minPrice,prices[i-1])#最小的成本是当前的之前的最小成本和前一天的成本（不能在同一天买入卖出）
            dp[i]=max(dp[i-1],prices[i]-minPrice)#根据递推公式计算
        return dp[-1]#返回最大值
