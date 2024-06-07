#https://leetcode.cn/problems/copy-list-with-random-pointer/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：利用哈希表来存储已经遍历过的节点，然后再次遍历节点时，random指向的节点就可以从hmap中取出。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return head#当链表为空，直接返回即可
        hmap={}#初始化哈希表
        cur=head#将cur指向头节点
        while cur:#第一次遍历链表，在哈希表中构建(原cur节点，新cur节点)
            hmap[cur]=Node(cur.val)
            cur=cur.next
        cur=head#将cur重新指向头节点
        while cur:#第二次遍历链表，hmap[cur]取出新的cur节点，将cur节点的next指向和random指向进行构建
            hmap[cur].next=hmap.get(cur.next)
            hmap[cur].random=hmap.get(cur.random)
            cur=cur.next
        return hmap[head]#返回新链表的头节点
