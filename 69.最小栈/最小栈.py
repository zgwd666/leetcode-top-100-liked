#https://leetcode.cn/problems/min-stack/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用两个栈实现常数时间的最小栈。

栈stack作为正常的栈，用于实现栈的出栈、入栈、查看栈顶元素等操作。

栈min作为存放最小值的栈，当入栈的值不大于min栈的栈顶元素时，元素入栈，当入栈的值大于min栈的栈顶元素时，当前栈的最小值无论如何都不会是该元素（先进后出，它一定会比当前min栈的栈顶元素先出栈），所以就不入min栈。

在出栈时，如果当前出栈的元素等于min栈顶元素，min栈顶元素同时出栈。
'''
class MinStack:

    def __init__(self):
        self.stack=[]#正常栈用于实现栈的出栈、入栈、查看栈顶元素等操作。
        self.min=[]#栈min作为存放最小值的栈

    def push(self, val: int) -> None:
        self.stack.append(val)#正常栈正常入栈
        #当入栈的值不大于min栈的栈顶元素时，元素入栈，当入栈的值大于min栈的栈顶元素时，当前栈的最小值无论如何都不会是该元素（先进后出，它一定会比当前min栈的栈顶元素先出栈），所以就不入min栈。
        if self.min and self.min[-1]<val:
            pass
        else:
            self.min.append(val)

    def pop(self) -> None:
        val=self.stack.pop()#正常栈出栈
        if val==self.min[-1]:#在出栈时，如果当前出栈的元素等于min栈顶元素，min栈顶元素同时出栈。
            self.min.pop()


    def top(self) -> int:
        return self.stack[-1]#返回栈顶元素


    def getMin(self) -> int:
        return self.min[-1]#返回栈中的最小元素



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
