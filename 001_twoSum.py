"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

举例：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

输入：nums = [3,2,4], target = 6
输出：[1,2]

输入：nums = [3,3], target = 6
输出：[0,1]
"""


class Solution:
    def twoSum(self, nums, target):
        for i, value in enumerate(nums):
            # 注意考虑到nums中两个相等数的情况，需要排除第一个索引
            if (target - value) in nums and i != nums.index(target - value):
                return [i, nums.index(target - value)]


# 直接数组的解法较耗内存，可采用下述哈希映射方法求解


class Solution2:
    def twoSum(self, nums, target):
        hashtable = dict()
        for i, value in enumerate(nums):
            # 将nums中的index及value的映射关系写入哈希映射中
            # 之所以将value作为key，i作为value是为了下面处理省事，当然倒过来也是可以的
            hashtable[value] = i
        for i, value in enumerate(nums):
            # 这里与Solution不同的地方就在于，可以通过get方法取字典中的值，大大降低用时
            if hashtable.get(target - value) and hashtable[target - value] != i:
                return [i, hashtable[target - value]]
