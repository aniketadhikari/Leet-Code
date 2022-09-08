class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        top = len(nums) - 1
        while top >= 0:
            topAndOne = top - 1
            while topAndOne >= 0: 
                # print(nums[top] + nums[topAndOne])
                if (nums[top] + nums[topAndOne] == target): 
                    return [top, topAndOne]
                topAndOne -= 1
            top -= 1