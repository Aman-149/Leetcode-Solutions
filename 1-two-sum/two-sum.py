class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newnum={}
        for index,num in enumerate(nums):
            val=target-num
            if val in newnum:
                return [newnum[val],index]
            newnum[num]=index
        print(newnum)
        return []