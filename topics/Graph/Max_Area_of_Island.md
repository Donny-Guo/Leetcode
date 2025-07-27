# Max Area of Island

https://leetcode.com/problems/max-area-of-island/description/

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.

 

**Example 1:**

![img](./assets/maxarea1-grid.jpg)

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

**Example 2:**

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

 

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1`.

**Reflections**:

- similar to number of islands
- can do dfs/bfs, w/wo modifying grid



## Solution: bfs

```python
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    dq = deque()
                    area = 0
                    dq.append((r, c))
                    while dq:
                        row, col = dq.popleft()
                        area += 1
                        for i, j in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                            if (0 <= i < ROWS
                                and 0 <= j < COLS
                                and (i, j) not in visited
                                and grid[i][j] == 1):
                                visited.add((i, j))
                                dq.append((i, j))
                    res = max(res, area)
        return res
```

TC: O(m * n)

SC: O(m * n)



## Solution: dfs

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            area = 0
            if (0 <= r < ROWS
                and 0 <= c < COLS
                and grid[r][c] == 1 
                and (r, c) not in visited):
                visited.add((r, c))
                area += 1
                for row, col in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    area += dfs(row, col)
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res
```

TC: O(m * n)

SC: O(m * n)