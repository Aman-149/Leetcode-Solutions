class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        l=list(s)
        if s==" ":
            return " "
        vowels=["A","E","I","O","U","a","e","i","o","u"]
        while left<right:
            if l[left] not in vowels:
                left=left+1
            if l[right] not in vowels:
                right=right-1
            if l[left] in vowels and l[right] in vowels:
                l[left],l[right]=l[right],l[left]
                left+=1
                right-=1
        return "".join(l)