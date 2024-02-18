# Meeting Rooms III

### Problem Link
https://leetcode.com/problems/meeting-rooms-iii/

### Intuition

The problem needs us to track 3 things
1. Minimum number (identifier) of meeting rooms available to be allocated.
2. The current ongoing meetings with their end times and the meeting room they are using.
3. The frequency of room being used. 

The first step of the problem is to get all the meeting start times in sorted order.
Then assign the first meeting to the first room, remove this first room from the priority queue and add the end time of this meeting to the meetings to be tracked priority queue.

Now for rest of the meetings we can have 2 cases
1. The start time of meeting < soonest ending meeting we can get from the priority queue. This means that this meeting either needs to be delayed or need a new room.
    1.1 If all meeting rooms are not busy, i.e. the available meeting room queue is not zero, we take one room from this queue and assign this meeting for this queue and add this meeting end time to priority queue along with this room number.
    1.2 If all meeting rooms are busy, this means that this meeting needs to be delayed. Now take the soonest end meeting from the priority queue of meetings in progress being tracked. Change end time of this meeting taking the soonest ending meeting's time as the start time and adding original duration to it.Remove the soonest ending meeting from the queue. Add this meeting to the queue along with the room number of the soonest ending meeting. (This takes care of the fact that the meeting that was originally scheduled earlier and is delayed now gets the priority and required room number)

2. The start time of meeting >= soonest ending meeting we can get from the priority queue. This means that this meeting need not be delayed.
    2.1 We can remove all meetings from the queue that meets this criteria and release the room numbers to the room number queue. Now we get the room number from the room number priority queue and add this meeting with it's end time and the room number to meeting queue.

For all of these setps we also use the room number to update the frequency of usage of the room number.

From the frequency, we can get our desired room number as result.
