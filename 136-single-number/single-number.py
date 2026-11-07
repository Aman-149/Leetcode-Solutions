class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count=dict(Counter(nums))
        for key,value in count.items():
            if value==1:
                return (key)