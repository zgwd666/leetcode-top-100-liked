#https://leetcode.cn/problems/find-median-from-data-stream/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
定义一个栈stack存储加入的数据，定义一个常数mid记录中位数

在加入数据时，进行遍历，将待加入的数据加入到栈中合适的位置（按照升序，插入应该插入的位置），然后计算有序栈stack的中位数赋值给mid

再返回中位数时，直接返回mid就行
'''
class MedianFinder:

    def __init__(self):
        #定义一个栈stack存储加入的数据，定义一个常数mid记录中位数
        self.stack=[]
        self.mid=0
    def addNum(self, num: int) -> None:
        #初始化下标
        index=0
        while self.stack and index<len(self.stack) and self.stack[index]<num:#当栈非空且index在栈中且num大于当前下标的元素，index+1
            index+=1
        #当index处于的位置时第一个大于index的元素时，将num插入该位置
        self.stack.insert(index,num)
        #计算中位数并赋值给mid
        if len(self.stack)%2==1:
            self.mid=self.stack[len(self.stack)//2]
        else:
            self.mid=(self.stack[len(self.stack)//2]+self.stack[len(self.stack)//2-1])/2
    def findMedian(self) -> float:
        return self.mid#返回中位数
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
