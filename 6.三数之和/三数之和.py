#https://leetcode.cn/problems/3sum/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：采用双指针来替代三层循环。其中需要注意对重复元素的去重
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#先对数组进行一个排序
        res=[]#初始化结果
        for i in range(len(nums)-2):#进行遍历，遍历的元素是可能答案中最小值
            if nums[i]>0:#如果最小值都大于0，那三个和及之后的都大于0，直接跳出循环
                break
            if i>0 and nums[i]==nums[i-1]:#存在重复元素，直接跳过
                continue
            l,r=i+1,len(nums)-1#初始化左右指针，为i+1,最右侧
            target=0-nums[i]#计算左右指针需要的和
            while l<r:#进行遍历
                if nums[l]+nums[r]==target:#如果三者和为0，将结果加入结果列表中
                    res.append([nums[i],nums[l],nums[r]])
                    #将左右指针向内收缩
                    l+=1
                    r-=1
                    #分别去掉左右侧重复的值
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                #如果相加值小于0，则左侧向右移动，并且跳过重复的值
                elif nums[l]+nums[r]<target:
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                 #如果相加值大于0，则右侧向左移动，并且跳过重复的值
                else:
                    r-=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return res
