#https://leetcode.cn/problems/linked-list-cycle-ii/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
此类链表题目一般都是使用双指针法解决的，例如寻找距离尾部第k个节点、寻找环入口、寻找公共尾部入口等

算法流程

双指针第一次相遇：设两指针fast，slow指向链表头部head，fast每轮走两步，slow每轮走1步

1. 第一种结果：fast指针走过链表末端，说明链表无环，直接返回null

如果存在环，两个指针一定会相遇，因为每走一轮fast与slow的间距+1，fast最终会追上slow

2. 第二种结果：当fast==slow时，两指针在环中第一次相遇。

设链表一共有a+b个节点，其中链表头部到链表环入口有a个节点（不计入链表入口节点），链表环有b个节点：设两个指针分别走了f，s步，则有

fast走的步数时是slow步数的2倍，即f=2s

fast比slow多走了n哥环的长度，即f=s+nb(双指针都走过a步，然后在环内绕圈直到重合，重合时fast比slow多走环的长度整数倍)

上面的式子联立可以得到，f=2nb s=nb，即fast和slow指针分别走了2n，n个环的周长

目前情况分析：

- 如果让指针从链表头部一直向前走并统计步数k，则所有走到链表入口i节点时的步数是:k=a+nb(先走a步到入口节点，之后每绕一圈都会再次进入到入口节点)
- 目前，slow指针走过的步数为nb步，因此，我们只需要让slow走a步停下来，就可以找到环的入口
- 依然使用双指针法。我们构建一个指针，需要有如下刑侦：此指针和slow一起向前走a步之后，两个在入口节点重合。那么从哪里走到入口需要a步，答案是链表头部

双指针第二次相遇：

- slow指针位置不变，将fast指针重新指向链表的头部节点，slow和fast同时每轮向前走1步
- 当fast指着走到f=a时，slow指针走到s=a+nb，此时两指针重合，并同时指向链表环入口。

第二次相遇后，返回slow指针指向的节点即可
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:#输入空链表，返回None
            return 
        slow,fast=head,head#初始化快慢指针都指向head
        while True:#进行第一次遍历
            if not (fast and fast.next):return #如果存在终点也就是没有环，返回None
            fast,slow=fast.next.next,slow.next#fast每次走两步，slow每次走一步
            if fast==slow:#当fast遇到slow，此时slow一共走了nb步，跳出本次循环
                break
        fast=head#将快指针重新指向头节点
        while fast!=slow:#第二次遍历，两个指针每次向前走一步，当他们走了a步时会相遇，相遇的节点就是环的入口节点
            fast,slow=fast.next,slow.next
        return slow#返回入口节点 
