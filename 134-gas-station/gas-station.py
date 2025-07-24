class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0    # 연료탱크
        start = 0   # 출발지점

        # 안되는 조건을 알아보자.
        # gas의 합이 cost의 합보다 적으면 이 문제의 조건은 성립하지 않는다.
        if sum(gas) < sum(cost) :
            return -1

        for i in range(len(gas)) :
            tank += gas[i] - cost[i]    # 연료탱크에 gas만큼 넣고 cost만큼 뺀다
            if tank < 0 :               # 만약 목적지에 도착하기 전에 탱크에 연료가 남아있지 않다면
                tank = 0                # 초기화
                start = i + 1           # 출발지점을 옮긴다.
        
        return start