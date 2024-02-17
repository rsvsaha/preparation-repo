import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        
        heapq.heapify(max_heap)
        
        resullt = 0
        for i in range(0,len(heights)-1):
            prev_building = heights[i]
            next_building = heights[i+1]
            diff = next_building - prev_building
            result=i
            if diff<=0:
                continue
            bricks-=diff
            heapq.heappush(max_heap,-diff)
            if(bricks<0):
                max_used_bricks_in_one_go = -1*heapq.heappop(max_heap)
                ladders-=1
                bricks += max_used_bricks_in_one_go
            
            if ladders<0:
                return result
        
        return len(heights)-1
        