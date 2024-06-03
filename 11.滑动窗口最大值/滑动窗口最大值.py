#https://leetcode.cn/problems/sliding-window-maximum/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用单调栈的方法，其中单调栈用于存储元素的下标。算法具体流程为：

当当前的数值不大于单调栈最后一个元素下标的数值，则将当前的下标存入单调栈，否则将单调栈中所有小于当前数值的下标都弹出。

每次遍历时将之前窗口的第一个元素弹出，然后将当前元素进行判断入栈与否，并将当前单调栈第一个元素的数值加入结果中。
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]#初始化结果
        stack=[]#初始化单调栈
        for i in range(k):#先对第一个窗口内的元素进行遍历
            while stack and nums[i]>nums[stack[-1]]:#栈非空且当前元素大于栈中最后一个元素代表的数值，不断弹出最后一个元素
                stack.pop()
            stack.append(i)#弹出结束，将当前元素的下标加入到单调栈中
        res.append(nums[stack[0]])#将第一个窗口的最大值加入结果中
        for i in range(k,len(nums)):#从k开始遍历
            if i-stack[0]==k:#如果栈中的第一个元素是上一个窗口的第一个元素，弹出
                stack.pop(0)
            while stack and nums[i]>nums[stack[-1]]:##栈非空且当前元素大于栈中最后一个元素代表的数值，不断弹出最后一个元素
                stack.pop()
            stack.append(i)#弹出结束，将当前元素的下标加入到单调栈中
            res.append(nums[stack[0]])#将本窗口的最大值加入到结果中
        return res#返回结果
