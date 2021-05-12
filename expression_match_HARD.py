#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:31:48 2021

@author: Viktor Semenov
"""
'''
Difficulty = Hard
'''
'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false
 

Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
Accepted
538,401
Submissions
1,955,382
'''
'''
below solution is not the fastest, but took only 5 minutes to make and it is not the slowest
'''
class Solution:
    def isMatch(self, s, p) -> bool:
        import re
        if '*' not in p and len(s)!=len(p):
            return False
        else:
            x=re.findall(p, s)
            if s in x:
                return True
            else:
                
                return False

y=Solution()
#F-T_T_T-F
s = "aa"
p = "a"
print(y.isMatch(s, p))
s = "aa"
p = "a*"
print(y.isMatch(s, p))
s = "ab"
p = ".*"
print(y.isMatch(s, p))
s = "aab"
p = "c*a*b"
print(y.isMatch(s, p))
s = "mississippi"
p = "mis*is*p*."
print(y.isMatch(s, p))      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
