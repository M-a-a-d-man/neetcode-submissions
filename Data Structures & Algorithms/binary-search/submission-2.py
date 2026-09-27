class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        m = r // 2

        while  l <= r:
            print(m)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
                m = (l+r) // 2
            else:
                r = m - 1
                m = (l+r) // 2
        
        return -1
        