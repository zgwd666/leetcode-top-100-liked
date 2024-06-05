#https://leetcode.cn/problems/reverse-linked-list/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：定义两个节点，一个指向None，一个指向head，在每次遍历时将cur节点的next指向pre，之后返回pre即可
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return#链表为空，直接返回
        #定义两个节点，一个指向None，一个指向head
        cur=pre=None
        cur=head
        #遍历链表
        while cur:
            temp=cur.next#先将cur.next存储起来
            cur.next=pre#将cur.next指向前一个节点
            pre=cur#将pre移动到当前节点
            cur=temp#将当前节点向后移动
        return pre#返回反转后的头节点
