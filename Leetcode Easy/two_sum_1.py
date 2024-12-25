#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        rep = {}
        for i, num in enumerate(nums):
            if target - num in rep:
                return [rep[target - num], i]
            rep[num] = i
        
# @lc code=end

