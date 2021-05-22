#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 08:49:07 2021

@author: user
"""
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
Accepted
575,365
Submissions
1,492,103
'''
'''
The trick of this task is to understand that no matter of zigzag pattern 
every character does occupy a row without any gaps.
All we need is to go back and forth with rows
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
            lines = dict((row,"") for row in range(numRows))
            
            row, direction = 0, 1
            for c in s:
                lines[row] += c
                row += direction
                
                if row >= numRows:
                    row = max(0,row-2)
                    if row != 0:
                        direction = -1
                elif row <= 0:
                    direction = 1
                
            return ''.join(lines[row] for row in range(numRows))
                
                


y=Solution()
# s = "PAYPALISHIRING"
# numRows = 3
# print(y.convert(s, numRows))
s = "PAYPALISHIRING"
numRows = 4
print(y.convert(s, numRows))
# s = "A"
# numRows = 1
# print(y.convert(s, numRows))






















