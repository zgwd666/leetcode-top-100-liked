#https://leetcode.cn/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
本题是跟求前缀和是一样的。
对于本题，定义两个前缀乘积数组，一个从左向后计算每一个元素的前缀乘积；一个从右向左计算每个位置的前缀和。然后将两个数组当前位置的前缀和进行相乘即可。
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)#定义左前缀乘积数组，初始化全为1
        right=[1]*len(nums)#定义右前缀乘积数组，初始化全为1
        res=[1]*len(nums)#定义结果数组，初始化全为1
        for i in range(1,len(nums)):#从左向右计算每个位置的前缀和
            left[i]=left[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):#从右向左计算每个位置的前缀和
            right[i]=right[i+1]*nums[i+1]
        for i in range(len(nums)):#遍历，计算每个位置除自身以外数组的乘积
            res[i]=left[i]*right[i]
        return res#返回结果
