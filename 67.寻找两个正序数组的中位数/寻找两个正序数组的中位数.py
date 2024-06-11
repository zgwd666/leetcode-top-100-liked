#https://leetcode.cn/problems/median-of-two-sorted-arrays/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：先用一个新的数组将nums1和nums2按升序组合起来。然后计算新数组的中位数即可
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]#创建一个空数组
        i,j=0,0#初始化i，j为0，指向nums1和nums2的首位
        while i<len(nums1) and j<len(nums2):#当nums1和nums2都没有超过范围时
            if nums1[i]<nums2[j]:#当前1中的数字小，先将1中的数字加入新数组，i+1
                nums.append(nums1[i])
                i+=1
            else:#当前2中的数字小，先将2中的数字加入新数组，j+1
                nums.append(nums2[j])
                j+=1
        if nums1[i:]:#当遍历完成后，1中还剩数据，将1中的数据加入新数组
            for num in nums1[i:]:
                nums.append(num)
        else:#当遍历完成后，2中还剩数据，将2中的数据加入新数组
            for num in nums2[j:]:
                nums.append(num)
        if len(nums)%2==1:#新数组的个数为奇数，直接返回最中间的值
            return nums[len(nums)//2]
        else:#新数组的个数为偶数，直接返回最中间两个值的平均值
            return ( nums[len(nums)//2]+ nums[len(nums)//2-1])/2
