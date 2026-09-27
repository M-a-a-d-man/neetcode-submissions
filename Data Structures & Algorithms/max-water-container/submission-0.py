class Solution:
    def maxArea(self, heights: List[int]) -> int:

        areas = []
        n = len(heights)
        for i in range(n):
            temp = [0]
            for j in range(i+1,n):
                l = j - i 
                w = min(heights[j],heights[i])
                A = l*w
                temp.append(A)
            largest = max(temp)
            areas.append(largest)
        
        return max(areas)

        