class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newLen = len(nums) *2
        ans = [0] * newLen
        k = 0
        for i in range(len(nums)):
            ans[i] = nums[i]
            k+=1
        for i in range(len(nums)):
            ans[k] = nums[i]
            k+=1
        return ans