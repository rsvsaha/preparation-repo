class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start_val = float('-inf')
        end_val = 0
        for weight in weights:
            start_val = max(start_val, weight)
            end_val += weight
        
        # We have got the search space now we need to define the fit criteria
        
        def is_solution_fitting(capacity):
            # Since one day is required at minimum for any capacity and we are incrementing it only when the load exceeds capacity
            days_required = 1
            capacity_loaded = 0
            for weight in weights:
                if capacity_loaded+weight>capacity:
                    days_required+=1
                    capacity_loaded = weight
                else:
                    capacity_loaded+=weight
                #Greater than permitted date
                if days_required>days:
                    return False
            # print(capacity,days_required)
            return True
        ans = -1
        while(start_val<=end_val):
            candidate_capacity = start_val + (end_val-start_val)//2
            if(is_solution_fitting(candidate_capacity)):
                ans = candidate_capacity
                # Try to optimize
                end_val = candidate_capacity - 1
            else:
                start_val = candidate_capacity + 1
        
        return ans