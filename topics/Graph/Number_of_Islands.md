# Number of Islands

https://leetcode.com/problems/number-of-islands/description/

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

 

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.



Questions to ask:

- can I modify the grid?
- Can grid be empty?

## Solution1: dfs without modifying grid

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if (0 <= row < ROWS
                and 0 <= col < COLS
                and (row, col) not in visited
                and grid[row][col] == '1' ):
                visited.add((row, col))
                for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                    dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visited
                    and grid[r][c] == '1'):
                    dfs(r, c)
                    res += 1
        
        return res
```

TC: O(m * n)

SC: O(m * n)





## Solution2: bfs without modifying grid

```python
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    visited.add((r, c))
                    dq = deque([(r,c)])
                    while dq:
                        row, col = dq.popleft()
                        for new_row, new_col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                            if (0 <= new_row < ROWS
                                and 0 <= new_col < COLS
                                and (new_row, new_col) not in visited
                                and grid[new_row][new_col] == '1'):
                                dq.append((new_row, new_col))
                                visited.add((new_row, new_col))
                    res += 1
        return res
```

TC: O(m * n)

SC: O(m * n)