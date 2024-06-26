class Solution:
    def reverse(self, x: int) -> int:
        # Initialized variable to store reversed number
        rev = 0
        
        # Case: Positive number
        if x>0:
            while x!=0:
                # Extracting the last digit of x
                num = x%10
                
                # Reversing number
                rev = rev * 10 + num

                # Removing the last digit from x
                x=x//10
            
            # Checking if reversed number exceeds 32-bit signed integer range
            if rev < -2**31 or rev > 2**31 - 1:
                # Return 0 if out of range
                return 0
            
            # Return reversed number
            else: return rev
       
        # Case: Negative number
        elif x<0:
            x = abs(x)
            while x!=0:
                num = x%10
                rev = rev * 10 + num
                x=x//10
            
            # Check if reversed number exceeds 32-bit signed integer range
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            else: return -rev
        else: return 0