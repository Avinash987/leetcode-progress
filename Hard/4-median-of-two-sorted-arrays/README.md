# 4. Median of Two Sorted Arrays

**Difficulty:** Hard  
**Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

## Approach

Use binary search on the smaller array to find the correct partition point that divides both arrays into two halves such that all elements on the left are smaller than all elements on the right.

**Algorithm:**
1. Ensure nums1 is the smaller array (swap if needed)
2. Use binary search on nums1
3. For each partition of nums1, calculate the corresponding partition of nums2
4. Check if we have the correct partition:
   - maxLeft1 <= minRight2 and maxLeft2 <= minRight1
5. If left side has too many elements, search left half
6. If right side has too many elements, search right half
7. Once found, calculate median based on total length (odd/even)

## Complexity

- **Time Complexity:** O(log(min(m, n))) - Binary search on smaller array
- **Space Complexity:** O(1) - Constant extra space

## Notes

This is one of the hardest problems on LeetCode. The key insight is using binary search on the smaller array to achieve logarithmic time complexity. Alternative O(m+n) solution using merge would be simpler but doesn't meet the time requirement.
