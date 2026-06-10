class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        for i in range(len(s)):
            a=list(s[i])
            l=0
            r=len(a)-1
            while l<r:
                a[l],a[r]=a[r],a[l]
                l+=1
                r-=1
            s[i]="".join(a)
        return " ".join(s)
 