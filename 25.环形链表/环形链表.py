#https://leetcode.cn/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
定义两个指针，fast和slow，开始都指向head。然后fast每次走两步，slow每次走一步。

如果不存在环，那么fast一定会先走到None的位置，此时直接返回False即可

如果存在环，那么相当于fast每次都比slow多走了一个位置，那么在fast和slow在环中的时候，fast会在后面缩短与slow之间的距离，直到追到slow
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:return False#如果链表为空，那么就不可能存在环，直接返回False即可
        fast=slow=head#定义两个指针，fast和slow，开始都指向head
        while True:#开始遍历
            if not fast or not fast.next:return#如果不存在环，那么fast一定会先走到None的位置，此时直接返回False即可
            #fast每次走两步，slow每次走一步
            fast=fast.next.next
            slow=slow.next
            #如果存在环，那么相当于fast每次都比slow多走了一个位置，那么在fast和slow在环中的时候，fast会在后面缩短与slow之间的距离，直到追到slow
            if fast==slow:
                break
        return True#快指针追上慢指针，此时存在环，返回True
