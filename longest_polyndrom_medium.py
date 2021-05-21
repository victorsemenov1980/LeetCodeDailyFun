#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 20:44:54 2021

@author: user
"""

'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
'''
'''
Solution is to be made faster,but it is working
Need to add up dict with plindromes
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_polindrom(s):
            if len(s)%2==0:
                firstpart, secondpart = s[:len(s)//2], s[len(s)//2:]
                
            else:
                middle=len(s)//2
                firstpart, secondpart = s[:middle], s[middle+1:]
            if firstpart==secondpart[::-1]:
                return 1
            else:
                return 0
        output=''
        temp=''
        i=0
        j=0
        
        while i in range(len(s)):
            
            temp+=s[i]
            
            if is_polindrom(temp)==1 and len(temp)>len(output):
                output=temp
                if i==len(s)-1:
                    
                    j+=1
                    i=j
                    temp=''
                else:
                    i+=1
            
            else:
                if i==len(s)-1:
                    
                    j+=1
                    i=j
                    temp=''
                else:
                    i+=1
       
            
                
        return output

y=Solution()
# s = "babad"
# print(y.longestPalindrome(s))
s = "cbbd"
print(y.longestPalindrome(s))
# s = "a"
# print(y.longestPalindrome(s))
# s = "ac"
# print(y.longestPalindrome(s))








