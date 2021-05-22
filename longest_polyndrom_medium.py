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

'''
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
'''
'''
This one is faster
moving centre
Runtime: 1732 ms, faster than 39.24% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.3 MB, less than 61.31% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        output=''
        
        for index in range(length):
            #odd poli
            left=index-1
            right=index+1
            while left>=0 and right<length and s[left]==s[right]:
                odd_polindrome=s[left:right+1]
                if len(odd_polindrome)>len(output):
                    output=odd_polindrome
                left-=1
                right+=1
            #even poli
            left=index
            right=index+1
            while left>=0 and right<length and s[left]==s[right]:
                even_polindrome=s[left:right+1]
                if len(even_polindrome)>len(output):
                    output=even_polindrome
                left-=1
                right+=1
            
        if output=='':
            output=s[0]
            
        return output

y=Solution()
s = "babad"

print(y.longestPalindrome(s))
s = "cbbd"
print(y.longestPalindrome(s))
s = "a"
print(y.longestPalindrome(s))
s = "aaaa"
print(y.longestPalindrome(s))

'''
even faster
Runtime: 1624 ms, faster than 40.26% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.4 MB, less than 37.39% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        output=''
        out_length=0
        
        for index in range(length):
            #odd poli
            left=index-1
            right=index+1
            while left>=0 and right<length and s[left]==s[right]:
                odd_polindrome=s[left:right+1]
                len_poli=len(odd_polindrome)
                if len_poli>out_length:
                    output=odd_polindrome
                    out_length=len_poli
                left-=1
                right+=1
            #even poli
            left=index
            right=index+1
            while left>=0 and right<length and s[left]==s[right]:
                even_polindrome=s[left:right+1]
                len_poli=len(even_polindrome)
                if len_poli>out_length:
                    output=even_polindrome
                    out_length=len_poli
                left-=1
                right+=1
            
        if output=='':
            output=s[0]
            
        return output

y=Solution()
s = "babad"

print(y.longestPalindrome(s))
s = "cbbd"
print(y.longestPalindrome(s))
s = "a"
print(y.longestPalindrome(s))
s = "aaaa"
print(y.longestPalindrome(s))

'''
even faster
Runtime: 1568 ms, faster than 40.93% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.4 MB, less than 61.31% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        output=''
        out_length=0
       
        for index in range(length):
            #odd poli
            left=index-1
            right=index+1
            while left>=0 and right<length and s[left]==s[right]:
                odd_polindrome=s[left:right+1]
                len_poli=right-left+1
                if len_poli>out_length:
                    output=odd_polindrome
                    out_length=len_poli
                left-=1
                right+=1
            #even poli
            left=index
            right=index+1
            while left>=0 and right<length and s[left]==s[right]:
                even_polindrome=s[left:right+1]
                len_poli=right-left+1
                if len_poli>out_length:
                    output=even_polindrome
                    out_length=len_poli
                left-=1
                right+=1
            
        if output=='':
            output=s[0]
            
        return output

y=Solution()
s = "babad"

print(y.longestPalindrome(s))
s = "cbbd"
print(y.longestPalindrome(s))
s = "a"
print(y.longestPalindrome(s))
s = "aaaa"
print(y.longestPalindrome(s))




