#
# @lc app=leetcode id=32 lang=python
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        result = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result,i-stack[-1])
        return result
        
# @lc code=end
