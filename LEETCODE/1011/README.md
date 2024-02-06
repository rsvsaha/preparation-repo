# Capacity To Ship Packages Within D Days

### Problem Link
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

### Intuition

We might be tempted to think that the average is a good starting point for search and we can use prefix sum somehow. But that is not the case.

The optimal solution will always lie between the maximum weight of a package and the sum of all the package weights.

The idea will be to apply a binary search on this problem space and optimizing it.

So, we can select the middle of the search space as a candidate. If using this candidate we get that it solves the constraints of loading the ship we will try to get a smaller candidate than this just to optimize on this. If it is not able to solve the constraint we will move to a bigger candidate. So in this way we can apply binary search on this.

