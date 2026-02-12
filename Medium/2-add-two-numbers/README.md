# 2. Add Two Numbers

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/add-two-numbers/

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Approach

Traverse both linked lists simultaneously, adding corresponding digits along with any carry from the previous addition.

**Algorithm:**
1. Create a dummy head node for the result
2. Initialize carry to 0
3. Iterate while there are nodes in either list or there's a carry
4. Add values from both lists (if they exist) plus the carry
5. Update carry and create new node with sum % 10
6. Move to next nodes in both lists
7. Return dummy.next

## Complexity

- **Time Complexity:** O(max(m, n)) - where m and n are lengths of the two lists
- **Space Complexity:** O(max(m, n)) - for the result linked list

## Notes

This problem teaches linked list manipulation and handling edge cases like different lengths and carry propagation.
