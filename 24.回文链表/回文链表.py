#https://leetcode.cn/problems/palindrome-linked-list/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：可以将链表转换为数组，检查数组是否为回文数组即可
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=[]#存储链表各个节点值的数组
        #对链表进行遍历，将值存入数组中
        while head:
            temp.append(head.val)
            head=head.next
        return temp==temp[::-1]#检查数组是否为回文数组即可
