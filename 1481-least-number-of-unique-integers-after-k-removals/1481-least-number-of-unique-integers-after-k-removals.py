import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        heap = [(freq, num) for num, freq in count.items()]
        heapq.heapify(heap)
        
        while k > 0 and heap :
            freq, num = heapq.heappop(heap)
            k -= freq
            
        if k < 0 :
            heap.append((freq, num))
            
        return len(heap)
        
# arr 에서  k 개 만큼 제거 하고 남아 있는 수의 개수를 리턴하라
# 1번 예시의 경우 5가 2개 4가 1개
# 1, 2 이기 때문에 k = 1 이니까 4 1개를 제거하고 5 하나만 남김.
# => len(set(arr)) 을 하면 1
# 2번 예시는 1, 3, 2, 1 이 나옴
# 빈도수 내림차순으로 정렬하면 1 1 2 3 이 됨
# k = 3 이므로 적은 수부터 1 1 을 제거함. 
# 2를 제거하면 k 를 초과하게 되므로 앞의 1 1 을 제거 => 4, 2 를 제거
# => len(set(arr)) 을 하면 1과 3이 남으므로 2가 리턴됨
