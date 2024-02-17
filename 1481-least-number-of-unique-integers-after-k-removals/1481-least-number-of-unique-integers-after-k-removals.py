class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Dictionary to track the frequencies of elements
        map = {}
        for i in arr:
            map[i] = map.get(i, 0) + 1

        n = len(arr)

        # List to track the frequencies of frequencies
        # The maximum possible frequency of any element
        # will be n, so we'll initialize this list with size n + 1
        count_of_frequencies = [0] * (n + 1)

        # Populating count_of_frequencies list
        for count in map.values():
            count_of_frequencies[count] += 1

        # Variable to track the remaining number of unique elements
        remaining_unique_elements = len(map)

        # Traversing over all possible frequencies
        for i in range(1, n + 1):
            # For each possible frequency i, we'd like to remove as
            # many elements with that frequency as possible.
            # k // i represents the number of maximum possible elements
            # we could remove with k elements left to remove.
            # count_of_frequencies[i] represents the actual number of elements
            # with frequency i.
            num_elements_to_remove = min(k // i, count_of_frequencies[i])

            # Removing the maximum possible elements
            k -= (i * num_elements_to_remove)

            # num_elements_to_remove is the count of unique elements removed
            remaining_unique_elements -= num_elements_to_remove

            # If the number of elements that can be removed is less
            # than the current frequency, we won't be able to remove
            # any more elements with a higher frequency so we can return
            # the remaining number of unique elements
            if k < i:
                return remaining_unique_elements

        # We have traversed all possible frequencies i.e.,
        # removed all elements. Returning 0 in this case.
        return 0
        
# arr 에서  k 개 만큼 제거 하고 남아 있는 수의 개수를 리턴하라
# 1번 예시의 경우 5가 2개 4가 1개
# 1, 2 이기 때문에 k = 1 이니까 4 1개를 제거하고 5 하나만 남김.
# => len(set(arr)) 을 하면 1
# 2번 예시는 1, 3, 2, 1 이 나옴
# 빈도수 내림차순으로 정렬하면 1 1 2 3 이 됨
# k = 3 이므로 적은 수부터 1 1 을 제거함. 
# 2를 제거하면 k 를 초과하게 되므로 앞의 1 1 을 제거 => 4, 2 를 제거
# => len(set(arr)) 을 하면 1과 3이 남으므로 2가 리턴됨
