class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if the total number of cards is divisible by groupSize 
        if len(hand) % groupSize :
            return False

        # Count the occurrences of each card value
        cnt = {}
        for n in hand :
            cnt[n] = 1 + cnt.get(n, 0)
        
        # Create a min-heap containing the unique card values
        minH = list(cnt.keys())
        heapq.heapify(minH)

        # Iterate through the min-heap
        while minH :
            first = minH[0] # Extract the smallest card value
            # Check each consecutive sequence of groupSize cards
            for i in range(first, first + groupSize) :
                # If a card is missing or has exhausted its occurrences, return False
                if i not in cnt :
                    return False
                cnt[i] -= 1
                if cnt[i] == 0 :
                    # Remove the card value from the min-heap if its occurrences are exhausted
                    if i != minH[0] :
                        return False
                    heapq.heappop(minH)
        return True