class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                new_pos = (i * n + j + k) % total
                result[new_pos // n][new_pos % n] = grid[i][j]

        return result