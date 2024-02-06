# Capacity To Ship Packages Within D Days

### Problem Link
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

### Intuition

We might be tempted to think that the average is a good starting point for search and we can use prefix sum somehow. But that is not the case.

The optimal solution will always lie between 1 (since minimum 1 product needs to be allocated to a shop and zero will not be considered) and maximum of the product frequency that is available.

The idea will be to apply a binary search on this problem space and optimizing it.

So, we can select the middle of the search space as a candidate. If using this candidate we get that it solves the constraints of dividing the product among shops we will try to get a smaller candidate than this candidate just to optimize on this candidate. If it is not able to solve the constraint we will move to a bigger candidate. So in this way we can apply binary search on this.

