class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre = [1] * length
        suf = [1] * length

        for i in range(length):
            if i == 0:
              pre[i] = 1
            elif i == 1:
                pre[i] = nums[i-1]  
            else:
                pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(-1,-length-1,-1):
            if i == -1:
                suf[i] = 1
            elif i == -2:
                suf[i] = nums[i+1]
            else:
                suf[i] = suf[i+1] * nums[i+1]

        # print(f"pre: {pre}")
        # print(f"suf: {suf}")
        res = []

        for i in range(length):
            res.append(pre[i] * suf[i])
        return res
