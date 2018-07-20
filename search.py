# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:09:23 2018

@author: lenovo
"""
#------------------------------------------------------------------------------
def Search(nums, target):
    if len(nums) == 0:
         return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
#------------------------------------------------------------------------------
testList = [5,6,7,1,2,3,4]
print(Search(testList, 1))