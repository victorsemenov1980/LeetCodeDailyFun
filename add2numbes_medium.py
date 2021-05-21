#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:27:29 2021

@author: user
"""

'''
You are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in reverse order,
 and each of their nodes contains a single digit. Add the two numbers 
 and return the sum as a linked list.

You may assume the two numbers do not contain any leading 
zero, except the number 0 itself.
'''

'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
'''
Below solution is very very slow, but extremely
memory efficient

Obviously with some additional memory it can go faster
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        l1n = ''
        while l1:
            l1n+=str(l1.val)
            l1 = l1.next
            
        l2n = ''
        while l2:
            l2n+=str(l2.val)
            l2 = l2.next
        
        summ=str(int(l1n[::-1])+int(l2n[::-1]))[::-1]
        
        
        head = ListNode()
        tmp = head
        
        for i,s in enumerate(summ):
            
            if i == 0:
                tmp.val = int(s)
            else:
                x = ListNode(int(s))
                tmp.next = x
                tmp = tmp.next
                
        return head