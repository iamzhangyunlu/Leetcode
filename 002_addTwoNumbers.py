"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

举例：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 注意合起来写是or，不是and
        if not (l1 or l2):
            return None
        # 如果l1是空的，补为0，同样下面l2一样
        if not l1:
            l1 = ListNode(val=0)
        if not l2:
            l2 = ListNode(val=0)
        # 将l2的节点值与l1相加
        l1.val += l2.val
        # 当加完和大于10需要进位
        if l1.val >= 10:
            # l1当前位置是除以10后的余数
            l1.val %= 10
            # 如果l1的下一个节点非空，值直接加在下一位
            if l1.next:
                l1.next.val += 1
            # 如果l1的下一个节点是空的，则直接新建一个节点，val为1
            else:
                l1.next = ListNode(val=1)
        # 循环执行此函数，l1.next依然如此，直到执行完整个链表长度
        l1.next = self.addTwoNumbers(l1.next, l2.next)
        # 每执行一次都返回当前节点运算后的值
        return l1
