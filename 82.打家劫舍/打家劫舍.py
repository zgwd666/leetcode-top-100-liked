#https://leetcode.cn/problems/house-robber/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用动态规划的思路

1.确定dp数组以及下标的含义

dp[i]:前i个房子在满足条件下能够偷窃到的最高金额

2.确定递推公式

dp[i]存在两种情况：

1.从dp[i-2]中获得，此时dp[i]=dp[i-2]+nums[i]

2.从dp[i-1]中获得，此时dp[i]=dp[i-1]

上面的dp[i-1]和dp[i-2]只是考虑nums[i-1]和nums[i-2]的情况，并不是必须要偷nums[i-1]和nums[i-2]

所以递推公式为：$$dp[i]=max(dp[i-2]+nums[i],dp[i-1])$$

3.初始化

$$dp[0]=nums[0]  dp[1]=max(nums[0],num[1])$$

4.确定遍历顺序

从前向后进行遍历
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:#只有1个或2个房子，返回其中的最大值就可以
            return max(nums)
        dp=[nums[0]]*len(nums)#创建dp数组
        dp[1]=max(nums[0],nums[1])#初始化
        for i in range(2,len(nums)):#进行遍历
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])#根据递推公式计算
        return dp[-1]#返回结果
