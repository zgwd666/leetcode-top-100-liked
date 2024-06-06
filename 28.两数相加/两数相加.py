#https://leetcode.cn/problems/add-two-numbers/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路
采用双指针。

创建两个伪节点和一个十位数计数。

对l1和l2和十位数计数进行遍历，当l1和l2未空且十位数计数为0时跳出遍历。

当前位置的和等于l1在此位置的值（如果存在否则为0）+l2在此位置的值（如果存在否则为0）+s

当前节点值为当前位置的和%10

s为当前位置的和//10

l1和l2 cur向后移动

返回dum.next 就是结果
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s=0#十位数计数
        dum=cur=ListNode(-1)#两个伪节点
        #对l1和l2和十位数计数进行遍历，当l1和l2未空且十位数计数为0时跳出遍历。
        while s or l1 or l2:
            tempVal=(l1.val if l1 else 0)+(l2.val if l2 else 0)+s#当前位置的和等于l1在此位置的值（如果存在否则为0）+l2在此位置的值（如果存在否则为0）+s
            cur.next=ListNode(tempVal%10)#节点值为当前位置的和%10
            s=tempVal//10#s为当前位置的和//10
            #l1和l2 cur向后移动
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            cur=cur.next
        return dum.next#返回结果
