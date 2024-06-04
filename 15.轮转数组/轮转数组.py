#https://leetcode.cn/problems/rotate-array/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：k如果大于数组的长度，在数组数字整体一轮轮转后会回到原来的位置。所以我们只需要计算k%len(nums)的部分也就是真正移动的位置。

对于这一部分，按照题意，也就是将后面的k个元素直接搬运到数组的前面即可
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)#去除无意义的轮转，计算真正有效的部分
        nums[:]=nums[-k:]+nums[:-k]#将nums切分为两个部分，后k个元素和之前的元素，将后k元素切开搬运到前面即可
