class Solution:
    def reverse(self, x: int) -> int:
        rev, num = 0, 0
        if x < 0:
            num = -1 * x
        elif x > 0:
            num = x
        else:
            return x
        while num > 0:
            rev = rev * 10 + num%10
            num = num //10 
        
        if rev > 2**31:
            return 0
        elif x < 0 :
            return -1 * rev
        else:
            return rev