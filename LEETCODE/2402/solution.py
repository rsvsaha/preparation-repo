import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        room_freq = [0] * n
        room_heap = []
        meetings = sorted(meetings, key = lambda x: x[0])
        for i in range(n):
            room_heap.append(i)
        heapq.heapify(room_heap)
        
        meeting_in_progress_heap = []
        
        heapq.heapify(meeting_in_progress_heap)
        [mstart,mend] = meetings[0]
        
        heapq.heappush(meeting_in_progress_heap,(mend,0))
        heapq.heappop(room_heap)
        
        room_freq[0]+=1
        for i in range(1,len(meetings)):
            
            [mstart,mend] = meetings[i]
            # This means an over lapping meeting
            if mstart < meeting_in_progress_heap[0][0]:
                # Meeting rooms are full
                if len(room_heap) == 0:
                    [soonest_end,room_number] = heapq.heappop(meeting_in_progress_heap)
                    diff = mend - mstart
                    new_mend = soonest_end+diff
                    heapq.heappush(meeting_in_progress_heap,(new_mend,room_number))
                    room_freq[room_number]+=1
                    
                else:
                    room_number = heapq.heappop(room_heap)
                    heapq.heappush(meeting_in_progress_heap,(mend,room_number))
                    room_freq[room_number]+=1
            # All meetings with timing >= soonest ending meeting
            else:
                # Free up all rooms
                while(len(meeting_in_progress_heap)>0 and mstart>=meeting_in_progress_heap[0][0]):
                    _,free_room_number = heapq.heappop(meeting_in_progress_heap)
                    # Return this room back to the heap
                    heapq.heappush(room_heap,free_room_number)
                room_number = heapq.heappop(room_heap)
                heapq.heappush(meeting_in_progress_heap,(mend,room_number))
                room_freq[room_number]+=1
        
        
        result = 0
        for i in range(1,n):
            if room_freq[i]>room_freq[result]:
                result=i
        
        return result
