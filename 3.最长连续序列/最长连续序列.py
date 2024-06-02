#https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：可以先将数组进行排序，然后从头开始遍历数组，如果存在连续序列的话，则后一个值等于前一个值+1，如果存在重复的值，直接跳过即可。
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<2:#当数组中仅存一个或零个数字，那么连续序列的长度就是此时数组的长度
            return len(nums)
        nums.sort()#对数组进行排序
        maxLength=curLength=1#初始化最长序列的长度和当前序列的长度为1，因为遍历从下标1开始
        for i in range(1,len(nums)):#从下标1开始遍历
            if nums[i]==nums[i-1]+1:#如果当前元素等于前一个元素+1，证明是连续的，当前连续序列的长度+1
                curLength+=1
            elif nums[i]==nums[i-1]:#如果遇到重复元素，直接跳过
                continue
            else:#如果前一个连续序列已经结束，则重置当前连续序列的长度为1
                curLength=1
            maxLength=max(curLength,maxLength)#计算最长序列的长度
        return maxLength#返回最长序列的长度
