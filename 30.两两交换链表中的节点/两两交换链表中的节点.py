#https://leetcode.cn/problems/swap-nodes-in-pairs/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
可以通过迭代的方式实现两两交换链表中的节点。

创建哑节点dum，令dum.next=head，创建一个临时节点cur表示当前到达的节点，初始时使得temp=dum，每次需要交换temp后面的两个节点。

如果temp后面没有节点或者只有一个节点，就不需要再进行节点交换，否则，获得temp后面的两个节点node1和node2，通过更新节点的指针关系实现两两交换节点了。

具体而言，交换之前的节点关系是temp->node1->node2,交换之后的节点关系变成temp->nod2->node1。

所有需要交换的节点交换完成之后，返回哑节点.next也即新的头节点即可
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head#当链表中为空或者仅有一个节点时，不需要进行交换，直接返回即可
        dum=cur=ListNode(-1)#创建一个哑节点和cur临时节点
        dum.next=head#将哑节点的next指向head
        while cur.next and cur.next.next:#如果temp后面没有节点或者只有一个节点，就不需要再进行节点交换，否则，获得temp后面的两个节点node1和node2，通过更新节点的指针关系实现两两交换节点了。
            temp=cur.next#存储cur下一个节点
            temp1=cur.next.next.next#存储交换节点后第一个当前不需要交换的节点
            cur.next=temp.next#将cur的next指向node2
            cur.next.next=temp#将node2的next指向node1
            temp.next=temp1#将node1的next指向粗出的temp1节点
            cur=cur.next.next#将cur移动到下一次需要交换的节点之前的节点
        return dum.next#返回交换后的头节点
