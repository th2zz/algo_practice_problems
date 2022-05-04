class Solution:  # https://leetcode.cn/problems/pacific-atlantic-water-flow/
    # 单元格上为海平面高度 water flows from high to low, 找到既能流到太平洋 也能流到 大西洋的坐标列表
    # left, top edges of the matrix are connected with the Pacific Ocean
    # right, bottom edges of the matrix are connected with Atlantic Ocean
    # return value: list[ coordinate], coordinate = [x1, y1]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            q = deque(starts)
            visited = set(starts)
            while q:
                x, y = q.popleft()
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and heights[nx][ny] >= heights[x][y]
                        and (nx, ny) not in visited
                    ):
                        q.append((nx, ny))
                        visited.add((nx, ny))
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, bfs(pacific) & bfs(atlantic)))
