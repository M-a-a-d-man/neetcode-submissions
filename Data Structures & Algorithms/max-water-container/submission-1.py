class Solution:
    def maxArea(self, heights: List[int]) -> int:

        areas = []
        n = len(heights)
        i = 0
        j = n-1

        while i != j:
            l = j - i 
            w = min(heights[j],heights[i])
            A = l*w
            areas.append(A)
            if w == heights[j]:
                j -= 1
            else:
                i += 1
            
        return max(areas)
        

        