# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 주어진 노드의 높이를 반환하는 동시에 높이 균형을 검사하는 함수
    def height(self, root: Optional[TreeNode]) -> bool:
        if root is None :   # 현재 노드가 None일 경우, 높이를 0으로 반환
            return 0
        leftValue = self.height(root.left)  # 왼쪽 자식 노드의 높이
        rightValue = self.height(root.right)    # 오른쪽 자식 노드의 높이

        # 왼쪽 또는 오른쪽 자식 노드의 높이 계산 결과가 -1이거나(불균형)
        # 왼쪽과 오른쪽 자식 노드의 높이 차가 1을 초과하는 경우 -1을 반환
        if leftValue == -1 or rightValue == -1 or abs(leftValue - rightValue) > 1 :
            return -1
        
        # 현재 노드의 높이는 자식 노드의 높이 중 큰 값에 1을 더한 값
        # 균형 상태일 경우 이 값을 반환한다.
        return 1 + max(leftValue, rightValue)
        
    # 주어진 트리가 높이 균형인지 판단하는 함수
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answer = self.height(root)  # 루트 노드부터 시작하여 트리의 높이 및 균형 상태를 확인
        if answer != -1 :   # 반환된 값이 -1이 아닌 경우. 트리가 높이 균형 상태임을 의미.
            return True
        return False