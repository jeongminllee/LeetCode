class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_sort = sorted(nums1 + nums2)
        n = len(merged_sort)
        if n % 2 == 1 :
            return merged_sort[n // 2]
        else :
            return (merged_sort[n // 2 - 1] + merged_sort[n // 2]) / 2