# Furthest Building You Can Reach

### Problem Link
https://leetcode.com/problems/furthest-building-you-can-reach/

### Intuition

We might be tempted to think that diff between building heights can be put in a heap or apply dp. But the problem is much simpler using MAX Heap.
The idea is there are 3 cases
if diff between buildings is <= 0, we can continue.
if diff between buildings > 0, we should use bricks to try to cross it. Now if it cannot be crossed using bricks, we use a ladder and restore the maximum bricks that has been used till in a step from the MAX HEAP and reduce ladders by 1 indicating that a ladder has been used. If the ladder becomes less than 0 means we have exhausted our ladders and that's maximum we could have gone.

So the idea is
for i in range(0,len(h)-1):
    diff = h[i+1] - h[i]
    if diff<=0:
        continue
    bricks-=diff 
    max_heap.push(bricks)
    if bricks < 0: #Bricks can become negative which means this case will require usage of a ladder and restore the max used bricks at one go from heap
        bricks+=max_heap.pop()
        ladder-=1
    if ladder<0: # Means all ladders have been used
        return i

return len(h)-1 # This case means the ladders have never gone negative and thus we have successfully exited the loop. So the last item must be the answer.


