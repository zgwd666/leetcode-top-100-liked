#https://leetcode.cn/problems/search-insert-position/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用二分查找的方法。目标值在数组中的位置存在四种情况：

1.目标值在所有的元素位置的前面

2.目标值在所有元素位置的后面

3.目标等于数组中某个元素

4.目标值在数组中某个元素的后面

定义在一个封闭的区间[left,ight]中，每次查找left和right中间位置的值与目标值进行对比，定位目标值的位置。存在如下两种情况：

1.当目标值等于数组中某个元素，就会在循环中遇到target==nums[mid]的情况，此时直接返回mid即可

2.当目标值不在数组中时，因为在数组中找不到该目标值，就会出现l>r以结束循环：针对剩余的三种情况，有：

1.目标值在所有的元素位置的前面：此时r=-1，l=0，目标值应该插入的位置是0也就是l的位置

2.目标值在所有元素的后面：此时r=n-1,l=n，目标值应该插入的位置是n也就是l的位置

3.目标值在某个元素的后面，此时l等于该元素+1，r等于该位置的位置，目标值应该插入的位置也就是该位置+1的位置也就是l的位置

综上，只要目标值不在数组中，应该返回l
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1#初始化左右边界
        while l<=r:#在闭区间内遍历
            mid=(r+l)//2#计算中间位置
            if nums[mid]==target:#如果中间位置的值等于目标值，直接返回中间位置
                return mid
            elif nums[mid]<target:#当中间位置的值小于目标值，l变为mid+1
                l=mid+1
            elif nums[mid]>target:#当中间位置的值大于目标值，r变为mid-1
                r=mid-1
        return l#当只要目标值不在数组中，应该返回l
