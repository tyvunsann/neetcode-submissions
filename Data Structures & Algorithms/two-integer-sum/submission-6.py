class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Given an array of integers nums and an integer "target"
        # Return the indices i and j such that nums[i] + nums[j] == target
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i