#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 14:22:47 2021

@author: Viktor Semenov
"""

'''
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
 

Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
Accepted
206,688
Submissions
779,604

'''
#Solution below is not trully fast, but exceptionally simple
class Solution:
    def findSubstring(self, s, words):
        #1st get and save all concats
        import itertools
        x=list(itertools.permutations(words, len(words)))
        combinations=[]
        for i in x:
            string=''
            for j in i:
                string+=j
            combinations.append(string)
        comb=len(combinations[0])
        #get indices of all combinations found
        import re
        output=[]
        for pattern in combinations:
            #make moving window as re.finditer searching next match at the end of the first match
            for i in range(0,(len(s)-comb)+1):
                
                for m in re.finditer(pattern, s[i:(comb+i)]):
                    if m.start(0) is not None:
                         output.append(m.start(0)+i)
                
                
                       
            
        f=set(output) 
        return list(f)

y=Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
print(y.findSubstring(s, words))
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(y.findSubstring(s, words))       
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(y.findSubstring(s, words))        
s="foobarfoobar"
words=["foo","bar"]       
print(y.findSubstring(s, words))  
s="aaa"
words=["a","a"]
print(y.findSubstring(s, words)) 
        
        
        
        
        
        
        
        
        
        
        
        