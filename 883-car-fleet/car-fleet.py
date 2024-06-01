class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars :
            times = (target - p) / s

            if stack and times <= stack[-1] :
                continue

            stack.append(times)

        return len(stack)