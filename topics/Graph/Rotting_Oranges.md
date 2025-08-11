# Rotting Oranges

https://leetcode.com/problems/rotting-oranges/description/

You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.

 

**Example 1:**

![img](./assets/oranges.png)

```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**

```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:**

```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

 

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.



**Reflections**:

- Multi-source BFS



## Solution

```python
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        dq = deque()
        count, time = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count += 1
                elif grid[r][c] == 2:
                    dq.append((r, c))
                    seen.add((r, c))
        if count == 0: return 0

        while count > 0 and dq:
            k = len(dq)
            time += 1
            for _ in range(k):
                r, c = dq.popleft()
                for row, col in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                    if ((0 <= row < ROWS) and
                        (0 <= col < COLS) and
                        ((row, col) not in seen) and
                        (grid[row][col] == 1)):
                        count -= 1
                        seen.add((row, col))
                        dq.append((row, col))
                    
        
        return time if count == 0 else -1
```

TC: O(m * n)

SC: O(m * n)