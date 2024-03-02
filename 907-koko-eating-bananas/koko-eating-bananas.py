class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k) :
            return sum((p - 1) // k + 1 for p in piles) <= h

        low = 1
        high = max(piles)
        while low < high :
            mid = (low + high) // 2
            if not possible(mid) :
                low = mid + 1
            else :
                high = mid

        return low