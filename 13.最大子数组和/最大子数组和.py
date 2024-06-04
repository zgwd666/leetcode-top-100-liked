#https://leetcode.cn/problems/maximum-subarray/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用动态规划。

1.确定dp数组以及下标的含义

dp[i]是在下标i处的所能获得的最大和

2.确定递推公式

因为是连续子数组，所以和要么加上之前的和，要么就是当前的值

dp[i]=max(dp[i-1],0)+nums[i]

3.初始化

dp[0]=num[0]

4.确定遍历顺序

从左向右遍历
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:#只有一个值，那最大的和就是第一个数字
            return nums[0]
        dp=[0]*len(nums)#创建状态转移数组
        dp[0]=nums[0]#初始化
        for i in range(1,len(nums)):#进行遍历
            dp[i]=max(dp[i-1],0)+nums[i]#根据递推公式进行计算
        return max(dp)#返回最大值
