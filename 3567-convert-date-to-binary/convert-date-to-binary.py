class Solution:
    def convertDateToBinary(self, date: str) -> str:
        a=date.split("-")
        print(a)
        for i in range(len(a)):
            b=bin(int(a[i]))
            a[i]=b[2:]
        return "-".join(a)