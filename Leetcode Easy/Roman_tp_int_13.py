#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        int_sum = 0
        prev_value = 0
        
        for char in reversed(s):  
            value = roman_to_int[char]
            if value < prev_value:
                int_sum -= value  # Subtract if smaller value precedes a larger value
            else:
                int_sum += value
            prev_value = value

        return int_sum
        
# @lc code=end

