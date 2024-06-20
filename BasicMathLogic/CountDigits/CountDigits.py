class Solution:
    def evenlyDivides (self, N):
        count = 0
        # Loop for iterating each digit of given number
        for digits in str(N):
            # Converting string to int for performing math operations
            digit = int(digits)
            # Loop to validate that its digit divide the given number
            if digit>0 and N%digit==0:
                # Updating count by 1 everytime the condition is met
                count+=1
        return count
