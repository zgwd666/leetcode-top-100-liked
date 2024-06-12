#https://leetcode.cn/problems/daily-temperatures/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用单调栈的思路。
从下标1开始遍历，如果当前下标的温度不大于stack栈顶元素的温度，当前下标入栈。否则一直将栈顶元素弹出，并记录下当前下标与栈顶下标之间的距离作为栈顶下标的结果。
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures)==1:#只有一个元素，返回[0]
            return [0]
        result=[0]*len(temperatures)#初始化结果矩阵
        stack=[0]#创建栈，下标0先入栈
        for i in range(1,len(temperatures)):#从下标1开始遍历
            if temperatures[i]<=temperatures[stack[-1]]:#如果当前下标的温度不大于stack栈顶元素的温度，当前下标入栈
                stack.append(i)
            else:#否则一直将栈顶元素弹出，并记录下当前下标与栈顶下标之间的距离作为栈顶下标的结果。
                while stack and temperatures[i]>temperatures[stack[-1]]:
                    index=stack.pop()
                    result[index]=i-index
                stack.append(i)
        return result#返回结果
