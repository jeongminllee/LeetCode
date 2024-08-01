class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_bits(n) :
            return bin(n).count('1')

        result = []
        for hour in range(12) :
            for minute in range(60) :
                if count_bits(hour) + count_bits(minute) == turnedOn :
                    result.append(f"{hour}:{minute:02d}")

        return result