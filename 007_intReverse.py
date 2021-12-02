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


# 简写方法


class Solution2:
    def reverse(self, x: int) -> int:
        # 先设置正负号的flag
        flag = 1 if x > 0 else -1
        # 通过字符串反转，与第一种方法其实是一样的，字符串反转可通过[::-1]或reverse()函数
        result = flag * int(str(abs(x))[::-1])
        # 最终结果的绝对值如果大于题目给定的边界值，则返回0
        if abs(result) > 2 ** 31:
            return 0
        # 否则返回1
        return result


# 位运算方法

class Solution3:
    def reverse(self, x):
        y = abs(x)
        res = 0
        while y:
            # 将y的数字部分一个个取余数，得到的数字按顺序先加入到res中，然后执行下面的 y//=10
            res = res * 10 + y % 10
            # 每次循环获取到res值之后，都需要判断一下当前res是否已经超出题目规定的边界了
            if abs(res) > 2 ** 31:
                return 0
            # y //= 10 表示 y = y // 10，//表示取商
            # y // 10 就表示除以10之后，得到的商，也就是剔除当前数字最后一位，还剩下的前面的数字
            # while 循环中不断地减一位，最终得到每一个数字
            y //= 10
        if x > 0:
            return res
        else:
            return -res


"""
举例：123

第一次循环：
res = 0 * 10 + 123 % 10 = 0 + 3 = 3
判断 3 小于边界
123 // 10 得到 12（商，此时 3 已经被剔除掉了）

第二次循环
res = 3 * 10 + 12 % 10 = 30 + 2 = 32
判断 32 小于边界
12 // 10 得到 1

第三次循环
res = 32 * 10 + 1 % 10 = 320 + 1 = 321
判断 321 小于边界
1 // 10 得到 0

第四次循环已经走不进去了
最终判断反转后 res 的符号，返回最终结果
"""
