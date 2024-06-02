#https://leetcode.cn/problems/container-with-most-water/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
本题的面积计算公式为$$maxArea=min(heigt[l],heigjr[r])*(r-l)$$

所以可以采用双指针的方式。算法流程为：

1.定义两个指针l,r分别指向数组的首尾位置。

2.计算当前的面积，将当前的面积和之间计算的最大面积进行比较，更新最大面积。

3.找到当前的最短边，将其向里面收缩，进行下一步的迭代。
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxValue=0#初始化最大面积
        l,r=0,len(height)-1#创建左右指针
        while l<r:#进行遍历，当左右指针碰到一起跳出循环
            curValue=(r-l)*min(height[l],height[r])#计算当前的面积
            maxValue=max(maxValue,curValue)#更新最大的面积
            #找到当前的最短边，将其向里面收缩
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxValue#返回最大面积
