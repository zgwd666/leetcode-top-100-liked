#https://leetcode.cn/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
我们可以先遍历一次链表，获取链表的总长度，并计算出需要删除节点从前向后的位置

第二次进行遍历时，先定位到要删除节点的前一个节点。然后将前一个节点的next定义为前一个节点的next.next，实现跳过待删除节点，实现删除待删除节点的效果。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0#初始化链表的长度
        dum=ListNode(-1)#创建一个伪节点用来定义头节点的位置
        dum.next=head#伪节点的next指向head
        cur=head#cur指向head
        while cur:#进行遍历获取链表的长度
            count+=1
            cur=cur.next
        cur=dum#将cur指向dum，这是为了防止头节点是待删除的节点
        for i in range(count-n):#定位到待删除节点的前一个节点
            cur=cur.next
        cur.next=cur.next.next#将前一个节点的next定义为前一个节点的next.next
        return dum.next#返回删除后的头节点即可
