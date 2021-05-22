#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:02:48 2021

@author: user
"""

'''
You are given a string s. You can convert s to a palindrome by 
adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
Accepted
116,313
Submissions
376,379
'''
'''
SLow, but memory good
Runtime: 1264 ms, faster than 5.29% of Python3 online submissions for Shortest Palindrome.
Memory Usage: 14.5 MB, less than 72.36% of Python3 online submissions for Shortest Palindrome.\
'''
class Solution:
    def shortestPalindrome(self, s) -> str:
        #we cannot add on the right, so we have initial centre
        length=len(s)
        def is_poli(s):
            length=len(s)
            if length%2==0:
                middle=length//2-1
                if s[:middle+1]==s[middle+1:][::-1]:
                    return 1
                else:
                    return 0
            else:
                middle=length//2
                if s[:middle]==s[middle+1:][::-1]:
                    return 1
                else:
                    return 0
        if length==0:
            output=''
            
        elif length==1:
            output=s
            
            
        
        elif is_poli(s)==1:
            output=s
            
        else:
            big_poli=s[1:][::-1]+s
            output=big_poli
            for index in range(1,length):
                big_poli=s[index:][::-1]+s
                
                if is_poli(big_poli)==1:
                    output=big_poli
            
        return output

y=Solution()
s=["aacecaaa","abcd","",'aba',"abbacd","aabbaad"]
outs=["aaacecaaa","dcbabcd","",'aba',"dcabbacd","daabbaad"]
for i in range(len(s)):
    print(y.shortestPalindrome(s[i])==outs[i])




