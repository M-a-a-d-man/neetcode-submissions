class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        
        n = len(nums)
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        rev = {}
        for key,v in hashMap.items():
           rev[v] = key
        
        topFreq = sorted(list(rev.keys()), reverse=True)[:k]
        res = [] 
        for c in topFreq:
            for key, v in hashMap.items():
                if v == c:
                    res.append(key)
        
        return res[:k]

        

