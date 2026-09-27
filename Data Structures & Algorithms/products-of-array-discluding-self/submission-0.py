class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        suf = [1]*n
        
        
        for i in range(n):
            if i == 0:
               continue
            else:
                preProd = nums[i-1] * pre[i-1]
                pre[i] = preProd

                # when i = 1, we talk about suf at index 2 (n-i) so the suffix 
                sufProd = nums[n-i] * suf[n-i]
                suf[n-i-1] = sufProd
        res = []
        for i in range(n):
            res.append(pre[i] * suf[i])
        
        return res
        



        