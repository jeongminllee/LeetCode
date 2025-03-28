class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 단일 거래에서 최대 이익과 해당 매수, 매도 인덱스를 구하는 그리디 알고리즘 함수
        # 이 함수는 한 번의 거래로 얻을 수 있는 최대 이익을 계산하며, 배열을 한 번 순회합니다.
        def max_profit_with_index(prices) :
            min_price = float('inf')    # 현재까지의 최소 가격을 저장 (초기값: 무한대)
            max_profit = 0              # 현재까지의 최대 이익
            min_index = 0               # 최소 가격이 등장한 인덱스
            buy_index = 0               # 매수 인덱스 (최소 가격 발생 시점)
            sell_index = 0              # 매도 인덱스 (최대 이익 갱신 시점)

            # 가격 배열을 순회하며 현재까지의 최소 가격과 최대 이익을 계산
            for i, price in enumerate(prices) :
                if price < min_price :
                    min_price = price
                    min_index = i

                current_profit = price - min_price
                if current_profit > max_profit :
                    max_profit = current_profit
                    buy_index = min_index   # 최대 이익을 낼 때의 매수 시점 갱신
                    sell_index = i          # 최대 이익을 낼 때의 매도 시점 갱신

            # 한 번의 거레에서 최대 이익과 해당 거래의 매수, 매도 인덱스 반환
            return max_profit, buy_index, sell_index

        # 분할 정복 방식을 사용하여 전체 배열에서 가능한 모든 거래 이익을 찾아내는 재귀 함수
        # 여기서는 최대 이익 거래를 기준으로 배열을 좌측, 우측, 내부(역순)로 분할하여 재귀 호출합니다.
        def recur(prices, res) :
            # 거래를 진행할 수 없는 경우 (가격이 2개 미만) 종료
            if len(prices) < 2 :
                return 0

            # 그리디 알고리즘을 이용해 현재 배열에서 최대 이익 거래와 관련 인덱스 구하기
            profit, buy, sell = max_profit_with_index(prices)
            # 만약 이익이 0이면 더 이상 유의미한 거래가 없으므로 종료
            if profit == 0 :
                return

            # 현재 구간에서 발견한 최대 거래 이익을 결과 리스트에 추가
            res.append(profit)

            # 분할 정복 : 최대 거래를 기준으로 배열을 3개 구간으로 나누어 재귀적으로 처리
            # 1. 왼쪽 구간 : 최대 거래 시작 전의 가격들
            recur(prices[:buy], res)
            # 2. 오른쪽 구간 : 최대 거래 종료 후의 가격들
            recur(prices[sell + 1:], res)
            # 3. 내부 구간 : 최대 거래 구간 내부에서 발생할 수 있는 추가 거래 탐색
            #   내부 구간을 역순으로 뒤집어 재탐색하는 이유는, 내부에도 반대 방향의 가격 패턴이 있을 수 있기 때문입니다.
            tmp = list(reversed(prices[buy : sell]))
            recur(tmp, res)

        res = []
        # 전체 가격 배열에 대해 재귀적으로 모든 거래 이익을 찾아냅니다.
        recur(prices, res)
        # 모든 거래 이익을 내림차순으로 정렬한 후 상위 k개의 이익만 선택
        res.sort(reverse=True)

        # k번의 거래로 얻을 수 있는 최대 총 이익 반환
        return sum(res[:k])