#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    """
    1. Base case 를 모두 정의
    2. 전 단계를 기반으로 다음 단계가 어떻게 구성되는지 따져보기
    """
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        full = [0] * n
        top = [0] * n
        bottom = [0] * n
        if n == 1:
            return 1
        if n == 2:
            return 2
        full[0] = 1
        full[1] = 2
        top[1], bottom[1] = 1,1
        for i in range(2,n):
            top[i] = bottom[i-1] + full[i-2]
            bottom[i] = top[i-1] + full[i-2]
            full[i] = full[i-1] + full[i-2] + top[i-1] + bottom[i-1]
        return full[n-1] % MOD
    
    """
    - 2 단계 전만 기반으로 하므로, 2개 변수만 저장
    - Time : O(n)
    - Space : O(1)
    """
    def numTilings2(self, n : int) -> int:
        MOD = 10**9 + 7
        FF, F, T, B = 1, 1, 0, 0
        for i in range(2,n+1):
            FF, F, T, B = F, F+FF + T+B, B+FF , T+FF
        return F % MOD

# @lc code=end

