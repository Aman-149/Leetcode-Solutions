class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        fir=sum(nums[:k])
        maxi=fir
        for i in range(k,len(nums)):
            fir=fir+nums[i]-nums[i-k]
            maxi=max(maxi,fir)
        return maxi/k