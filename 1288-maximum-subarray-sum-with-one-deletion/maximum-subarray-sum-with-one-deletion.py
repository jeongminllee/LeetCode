class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        tmp = tmp_del = res = arr[0]
        for num in arr[1:] :
            tmp = max(tmp + num, num, tmp_del)
            tmp_del = max(tmp_del + num, num)
            res = max(res, tmp_del, tmp)

        return res