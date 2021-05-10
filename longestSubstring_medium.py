#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:22:13 2021

@author: Viktor Semenov
"""

'''
A medium difficulty problem
'''

'''

Given a string s, find the length of the longest substring 
without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
Accepted
2,178,037
Submissions
6,880,572
'''
class Solution: #below is pretty slow algorythm showed to be faster than 10% of submissions
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=''
        string_collection=0
        i=0
        j=0
        while i < len(s):
            if s[i] not in temp:
                temp+=s[i]
                if len(temp)>string_collection:
                    string_collection=len(temp)
                i+=1
                
            else:
                temp=''
                j+=1
                i=j
                
                
        return string_collection

# y=Solution()
# s="abcabcbb"
# print(y.lengthOfLongestSubstring(s))
# s = "bbbbb"
# print(y.lengthOfLongestSubstring(s))
# s = "pwwkew"
# print(y.lengthOfLongestSubstring(s))
# s=""
# print(y.lengthOfLongestSubstring(s))
# s=" "
# print(y.lengthOfLongestSubstring(s))
# s="dvdf"
# print(y.lengthOfLongestSubstring(s))

class Solution_even_slower: #below is the solution turned up to be even slower (about 8 percent) plus lots of memory usage
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=''
        string_collection=[]
        i=0
        j=0
        while i < len(s):
            if s[i] not in temp:
                temp+=s[i]
                string_collection.append(temp)
                i+=1
                
            else:
                temp=''
                j+=1
                i=j
        
                
        try:
            return len(max(string_collection, key=len))
        except:
            return 0

# y=Solution_even_slower()
# s="abcabcbb"
# print(y.lengthOfLongestSubstring(s))
# s = "bbbbb"
# print(y.lengthOfLongestSubstring(s))
# s = "pwwkew"
# print(y.lengthOfLongestSubstring(s))
# s=""
# print(y.lengthOfLongestSubstring(s))
# s=" "
# print(y.lengthOfLongestSubstring(s))
# s="dvdf"
# print(y.lengthOfLongestSubstring(s))

class Solution_finally_faster: #below is improved style. It is faster and takes much less memory (less than 80 percent)
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=''
        temp2=''
        i=0
        j=0
        while i < len(s):
            if s[i] not in temp:
                temp+=s[i]
                i+=1
                
            else:
                
                if len(temp2)<len(temp):
                    temp2=temp
                temp=''
                j+=1
                i=j
        if len(temp2)<len(temp):
            return len(temp)
        else:
            return len(temp2)
        
                
       

y=Solution_finally_faster()
s="abcabcbb"
print(y.lengthOfLongestSubstring(s))
s = "bbbbb"
print(y.lengthOfLongestSubstring(s))
s = "pwwkew"
print(y.lengthOfLongestSubstring(s))
s=""
print(y.lengthOfLongestSubstring(s))
s=" "
print(y.lengthOfLongestSubstring(s))
s="dvdf"
print(y.lengthOfLongestSubstring(s))











