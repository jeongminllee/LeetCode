class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []

        for num in nums1 :
            heapq.heappush(heap, [num + nums2[0], 0])

        while k and heap :
            sm, pos = heapq.heappop(heap)
            res.append([sm - nums2[pos], nums2[pos]])

            if pos + 1 < len(nums2) :
                heapq.heappush(heap, [sm - nums2[pos] + nums2[pos + 1], pos + 1])
            k -= 1
            


        return res