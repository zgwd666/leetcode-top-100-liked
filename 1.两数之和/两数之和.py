#https://leetcode.cn/problems/two-sum/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：采用哈希表用来降低时间复杂度。具体为：

使用一个哈希表用来存储已经遍历过的数值以及其对应的下标，在之后的遍历中，如果发现target-当前的数字已经在哈希表中出现，那么直接返回当前的下标和哈希表中对应的数值的下标，如果没有找到，就将当前的数值为key，下标为value的键值对存入哈希表中
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2 and nums[0]+nums[1]==target:#当数组中仅有两个数字且加起来等于target时，直接返回对应下标即可
            return [0,1]
        hmap={}#初始化哈希表
        for i in range(len(nums)):#对数组中的各个元素进行遍历
            if target-nums[i] in hmap:#当配对的数字已经遍历过，直接将二者的下标返回即可
                return [i,hmap[target-nums[i]]]
            else:
                hmap[nums[i]]=i#如果之前并没有遍历过，则将当前的数值以及下标存入
        return -1#找不到匹配的，直接返回-1
