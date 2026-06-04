class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        left,right=0,len(a)-1
        while left<=right:
            a[left],a[right]=a[right],a[left]
            left+=1
            right-=1
        b=" ".join(a)
        return b