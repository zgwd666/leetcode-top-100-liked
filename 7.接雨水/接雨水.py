#https://leetcode.cn/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：采用双指针的思路。一个容器能够盛水的最大面积也就是其左边界和右边界的最小值减去当前的高度。那么就可以采用两个数组，分别计算当前位置的左右边界的最大值，然后计算当前位置的盛水量即可。
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0]*len(height)#初始化左边界数组
        right=[0]*len(height)#初始化右边界数组
        left[0]=height[0]#初始化值
        right[-1]=height[-1]#初始化值
        for i in range(1,len(height)):#从左到右进行遍历，计算当前位置的左边界最大值
            left[i]=max(height[i],left[i-1])
        for i in range(len(height)-2,-1,-1):#从右到左进行遍历，计算当前位置的右边界最大值
            right[i]=max(height[i],right[i+1])
        res=0#初始化结果
        for i in range(len(height)):#对整个数组进行遍历，计算当前位置的盛水量并加入到结果中
            res+=min(left[i],right[i])-height[i]
        return res#返回结果
