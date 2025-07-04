# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 15:24:40 2025

@author: efemuratucarli
"""

# Time:  O(m+n)
# Space: O(1)

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        rightIndex = m+n-1
        nums2index = 0
        nums1index = m-1
        for index in range(m + n - 1):
            if nums2index < n:
                if nums2[n-1-nums2index] >= nums1[nums1index]:
                    nums1[rightIndex] = nums2[n-1-nums2index]
                    rightIndex -= 1
                    nums2index += 1
                else:
                    nums1[rightIndex] = nums1[nums1index]
                    nums1[nums1index] = 0
                    rightIndex -= 1
                    nums1index -= 1
            else:
                break
        
        if m + n == 1:
            if n > 0:
                nums1[0] = nums2[0]

##Test Cases
# sol = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# sol.merge(nums1,m,nums2,n)

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
# sol.merge(nums1,m,nums2,n)