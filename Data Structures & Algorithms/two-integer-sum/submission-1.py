class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for i, num in enumerate(nums):
            val = target - num
            
            if val in nums:
                if val in found and found[val] != i:
                    return [found[val],i]
                else:
                    found[num] = i
        return []        
                

            
        