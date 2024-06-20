class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        
        if x>0:
            while x!=0:
                num = x%10
                rev = rev * 10 + num
                x=x//10
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            else: return rev
        elif x<0:
            x = abs(x)
            while x!=0:
                num = x%10
                rev = rev * 10 + num
                x=x//10
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            else: return -rev
        else: return 0