#https://leetcode.cn/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
双指针。

创建两个伪节点，初始化为-1节点

对l1和l2进行遍历。看l1和l2当前节点值哪个小，就将cur指向节点，节点后移，直到l1或者l2为空跳出。然后将cur指向未空的链表即可。

最后返回dumn.next 就是结果
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #只要有list1和list2有一个为空，直接返回另一个即可
        if not list1:return list2
        if not list2:return list1
        dumn=cur=ListNode(-1)#创建两个伪节点
        while list1 and list2:#对list1和list2进行遍历
            if list1.val<list2.val:#当前list1的节点值比较小
                cur.next=list1#将cur指向list1
                list1=list1.next#list1向后移动
            else:#当前list2的节点值比较小
                cur.next=list2#将cur指向list2
                list2=list2.next#list2向后移动
            cur=cur.next#cur向后移动
        cur.next=list1 if list1 else list2#cur指向未空的链表即可。
        return dumn.next#返回合并后的链表的头节点即可
