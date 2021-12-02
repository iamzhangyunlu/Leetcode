"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−2^31, 2^31 - 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

举例
输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
"""


class Solution:
    def reverse(self, x: int) -> int:
        ll = []
        count = 0
        for num in str(x):
            if num == '-':
                continue
            count += 1
            ll.append(num)
        ll = reversed(ll)
        s = ''
        for l in ll:
            s += str(l)
        s = int(s)
        if count != len(str(x)):
            if -2 ** 31 <= -s <= 2 ** 31 - 1:
                return -s
            else:
                return 0
        else:
            if -2 ** 31 <= -s <= 2 ** 31 - 1:
                return s
            else:
                return 0
