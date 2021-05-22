#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 12:03:16 2021

@author: user
"""

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
Accepted
1,304,501
Submissions
4,576,232
'''

'''
Slow brutforce
'''
class Solution:
    def threeSum(self, nums):
        if len(nums)<3:
            return []
        else:
            out=[]
            import itertools
            indices=[x for x in range(0,len(nums))]
            combs=list(itertools.combinations(indices, 3))
            for i in combs:
                summ=[]
                for j in i:
                    summ.append(nums[j])
                
                if sum(summ)==0 and sorted(summ) not in out:
                    out.append(sorted(summ))
                    
            return out

y=Solution()
nums = [-1,0,1,2,-1,-4]
print(y.threeSum(nums))
nums = [0,0,0]
print(y.threeSum(nums))
# nums = [0]
# print(y.threeSum(nums))

'''
Faster
'''
class Solution:
    def threeSum(self, nums):
        if len(nums)<3:
            return []
        else:
            out=[]
            indices = {}
            nums=sorted(nums)
            
            for key ,value in enumerate(nums):
                indices[value]=key
                
            for first_ind,first_num in enumerate(nums):
                
                if first_num>0:#no reason to continue
                    break
                else:
                    for second_ind,second_num in enumerate(nums[first_ind+1:]):
                        
                        zero=-(first_num+second_num)
                        
                        if zero in indices.keys() and indices[zero]>first_ind+second_ind+1:
                            temp=sorted([zero,first_num,second_num])
                            if temp not in out:
                                out.append(temp)
                            
                  
            return out

y=Solution()
nums = [-1,0,1,2,-1,-4]
print(y.threeSum(nums))
# nums = [0,0,0]
# print(y.threeSum(nums))
# nums = [0]
# print(y.threeSum(nums))
