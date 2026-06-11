class Solution:
    def hammingWeight(self, n: int) -> int:
        a=str(bin(n))
        b=a.replace("0","").replace("b","")
        return len(b)