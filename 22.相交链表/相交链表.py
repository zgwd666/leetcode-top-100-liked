#https://leetcode.cn/problems/intersection-of-two-linked-lists/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：可以创建两个节点A，B分别指向HeadA，HeadB。

设HeadA到交点的长度为a，之后的长度为c

设HeadB到交点的长度为b，之后的长度为c。

如果A，B分别开始遍历，遍历完自身之后，再从HeadB，HeadA在开始遍历。则有

a+c+b=b+c+a

一定会在交点处相遇（如果存在节点，否则会在None处相遇）
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:#有一个链表为空，二者的交点只能是None
            return 
        A,B=headA,headB#可以创建两个节点A，B分别指向HeadA，HeadB。
        while A!=B:#A和B相等就是二者的交点开始的地方
            A=A.next if A else headB
            B=B.next if B else headA
        return A#返回交点节点
