class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=list(t)
        for i in s:
            if i not in a:
                return i
            else:
                a.remove(i)
        return "".join(a)