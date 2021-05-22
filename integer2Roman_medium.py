#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 10:53:00 2021

@author: user
"""

'''
Roman numerals are represented by seven different symbols: 
    I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, 
just two one's added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, 
which is XX + V + II.

Roman numerals are usually written largest to smallest 
from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is 
before the five we subtract it making four. The same principle 
applies to the number nine, which is written as IX. There are six 
instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Example 2:

Input: num = 4
Output: "IV"
Example 3:

Input: num = 9
Output: "IX"
Example 4:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999
'''
'''
Faster than 50%
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        conversion={0:'',1:'I',2:'II',3:'III',4:'IV',40:'XL',6:'VI',7:'VII',8:'VIII', 9:'IX',20:'XX',30:'XXX',60:'LX',70:'LXX',80:'LXXX', 50:'L', 90:'XC', 400:'CD', 900:'CM', 5:'V',10:'X',200:'CC',300:'CCC',600:'DC',700:'DCC',800:'DCCC',50:'L',100:'C',500:'D',1000:'M'}
        if num in conversion.keys():
            return conversion[num]
        else:
            
            
            #we need to parse the number on thousands, hundreds, tens, ones
            str_num=str(num)
            if len(str_num)==4:
                thousands=int(str_num[0])
                hundreds=int(str_num[1])*100
                tens=int(str_num[2])*10
                ones=int(str_num[3])
                return conversion[1000]*thousands+conversion[hundreds]+conversion[tens]+conversion[ones]
            elif len(str_num)==3:
                hundreds=int(str_num[0])*100
                tens=int(str_num[1])*10
                ones=int(str_num[2])
                return conversion[hundreds]+conversion[tens]+conversion[ones]
            elif len(str_num)==2:
                
                tens=int(str_num[0])*10
                
                ones=int(str_num[1])
                
                return conversion[tens]+conversion[ones]
            elif len(str_num)==1:
                ones=int(str_num[0])
                return conversion[ones]
                
           

num=[3,4,9,58,1994]
sol=['III','IV','IX','LVIII','MCMXCIV']
y=Solution()
for i in range(len(num)):
    print(y.intToRoman(num[i])==sol[i])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
