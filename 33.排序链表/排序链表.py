#https://leetcode.cn/problems/sort-list/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：利用数组排序。先将链表中的数值遍历到数组中，对数组进行排序，然后将排序后的数组重组为链表，返回重组后的链表即可。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head#当链表为空或者链表中只有一个元素，就不需要排序直接返回即可
        temp=[]#创建一个存储链表节点数值的数组
        dum=ListNode(-1)#创建哑节点用来定位结果链表的头节点
        cur=dum#创建临时节点
        while head:#遍历链表，将值存入数组中
            temp.append(head.val)
            head=head.next
        temp.sort()#数组元素排序
        for i in range(len(temp)):#进行遍历
            cur.next=ListNode(temp[i])#对每一个元素创建新节点，按照顺序进行连接
            cur=cur.next
        return dum.next#返回结果链表的头节点
