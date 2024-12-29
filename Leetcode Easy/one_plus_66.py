#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        my_list =[]
        my_string = ''
        
        for i in digits:
            my_string += str(i)
        
        my_string = int(my_string) + 1
        my_string = str(my_string)
        
        for i in my_string:
            my_list.append(int(i))
            
        return my_list
        
# @lc code=end

