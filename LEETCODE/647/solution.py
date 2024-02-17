class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(False)
            dp.append(row)
        
        #Intuition
        #i,j gives the length starting and ending index of the substring
        #If s[i] == s[j] and dp[i+1][j-1] == True
        #This means dp[i][j] i.e. substring starting at i and ending at j is a palindrome
        #The above condition only holds for substring lengths>2
        #For substring lengths <=2 we will have to fill up first
        # Substrings of length 1 are always palindromes
        # Substrings of length 2 are palindromes if s[i]==s[i+1]
        count = 0
        for i in range(n):
            dp[i][i] = True
            count+=1
            if i<n-1 and s[i]==s[i+1]:
                dp[i][i+1]=True
                count+=1
        
        #The idea would be to fill up all substrings that end at jth index first starting from i
        for j in range(2,n):
            for i in range(j-1):
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count+=1
        # print(dp)
        return count
            
                
                
                
        