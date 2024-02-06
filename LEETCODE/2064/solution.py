class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        #Since the problem requires us to find the minimum product that was given to any store
        start = 1
        end = max(quantities)
        
        def is_solution_fit(min_number):
            shops_required = 0
            for quantity in quantities:
                if quantity%min_number==0:
                    shops_required+=(quantity//min_number)
                else:
                    shops_required+=(quantity//min_number)+1
                if shops_required > n:
                    return False
            return True
        ans = -1
        while(start<=end):
            candidate = start+ (end-start)//2
            if is_solution_fit(candidate):
                ans = candidate
                #Try to reduce the search space
                end = candidate-1
            else:
                start = candidate + 1
        
        return ans