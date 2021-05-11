#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:37:22 2021

@author: Viktor Semenov
"""
'''
Complexity = Hard
'''
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
Accepted
937,027
Submissions
2,961,335
'''

'''
Results of below solution:
    
Runtime: 92 ms, faster than 64.31% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.4 MB, less than 78.54% of Python3 online submissions for Median of Two Sorted Arrays.
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        array=sorted(nums1+nums2)
        import statistics
        return statistics.median(array)
        
        
        
y=Solution()
nums1 = [1,3] 
nums2 = [2]
print(y.findMedianSortedArrays(nums1, nums2))
nums1 = [1,2]
nums2 = [3,4]
print(y.findMedianSortedArrays(nums1, nums2))
nums1 = [0,0]
nums2 = [0,0]
print(y.findMedianSortedArrays(nums1, nums2))
nums1 = []
nums2 = [1]
print(y.findMedianSortedArrays(nums1, nums2))
nums1 = [2]
nums2 = []
print(y.findMedianSortedArrays(nums1, nums2))     
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
