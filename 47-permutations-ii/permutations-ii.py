def permutations(iterable, r=None):
    # Convert input to a tuple to allow index-based operations
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r  # Set default r to len(iterable) if not provided
    if r > n:
        return  # If r > n, no permutations are possible
    
    indices = list(range(n))  # Indices of the input iterable
    cycles = list(range(n, n - r, -1))  # Cycle lengths for each position in the permutation
    yield tuple(pool[i] for i in indices[:r])  # Yield the first permutation
    
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1  # Decrease the current cycle
            if cycles[i] == 0:
                # Cycle is finished; rotate indices to the left and reset the cycle length
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                # Swap the i-th index with the next index in the cycle
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])  # Yield the next permutation
                break
        else:
            # If no break occurred, all cycles are complete, and we exit
            return

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        for per in permutations(nums, len(nums)) :
            if per in res :
                continue
            res.append(per)

        return res