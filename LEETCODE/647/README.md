# Palindromic Substrings

## Problem link 
https://leetcode.com/problems/palindromic-substrings/

### Intuition

Create a DP Table. Table(i,j) will always denote a substring starting at ith index of the given string and ending at jth index of the given string.
So for i==j the Table(i,j) = True. This means all substrings of length 1 are a palindrome.
Now for substrings of length 2.
So if(i==i+1), we can put Table(i,i+1) = True. This means these substrings of length 2 are palindromes.
Now for all substrings.length>2 we can apply the formula of if(i==j and DP[i+1][j-1]==True). This means this is a palindrome. i.e. If the last 2 chars are palindromes and the middle word is a palindrome. This entire word is a palindrome.

Now the trick in filling up the DP table is that fix j first and fill up all i. That is fill the DP Table column wise first.

The DP table in this case will always be an upper triangular matrix.

For example aabbac
The DP Table will be

1 1 0 0 0 0
0 1 0 0 1 0
0 0 1 1 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 0 0 1

### One Important Point

If the problem says proper substring then DPTable[0][len(string)-1] should not be counted as this is the entire word. Not a substring