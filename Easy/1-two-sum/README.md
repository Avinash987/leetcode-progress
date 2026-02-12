# 1. Two Sum

**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/two-sum/

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Approach

Use a hash map to store the numbers we've seen and their indices. For each number, check if `target - num` exists in the hash map.

**Algorithm:**
1. Create an empty hash map
2. Iterate through the array
3. For each number, calculate complement = target - num
4. If complement exists in hash map, return [hash_map[complement], current_index]
5. Otherwise, store current number and index in hash map

## Complexity

- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(n) - Hash map can store up to n elements

## Notes

This is one of the most popular LeetCode problems and a great introduction to hash maps for optimization.
