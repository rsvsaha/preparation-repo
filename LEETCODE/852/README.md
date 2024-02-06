# Peak Index in a Mountain Array

### Problem Link
https://leetcode.com/problems/peak-index-in-a-mountain-array/

### Intuition

This is a classic binary search problem

The constraints are required for the middle candidate known as element
1. The required element will follow element-1 < element < element+1
2. If element has this condition element  < element + 1, this means the answer lies on the right side so, l = element+1
3. If element has this condition element < element-1, this means the answer lies on the left side so, r = element-1