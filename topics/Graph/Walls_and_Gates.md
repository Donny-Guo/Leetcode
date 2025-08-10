# Walls and Gates

https://leetcode.com/problems/walls-and-gates/description/

You are given an `m x n` grid `rooms` initialized with these three possible values.

- `-1` A wall or an obstacle.
- `0` A gate.
- `INF` Infinity means an empty room. We use the value `231 - 1 = 2147483647` to represent `INF` as you may assume that the distance to a gate is less than `2147483647`.

Fill each empty room with the distance to *its nearest gate*. If it is impossible to reach a gate, it should be filled with `INF`.

 

**Example 1:**

![img](./assets/grid.jpg)

```
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

**Example 2:**

```
Input: rooms = [[-1]]
Output: [[-1]]
```

 

**Constraints:**

- `m == rooms.length`
- `n == rooms[i].length`
- `1 <= m, n <= 250`
- `rooms[i][j]` is `-1`, `0`, or `231 - 1`.



**Reflections**:

- instead of doing bfs from each room, do bfs on all the gates (multi-source bfs) -> do not revisit rooms and do it in O(m * n) time



## Solution:

```python
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        seen = set()
        distance = 0
        dq = deque()
        ROWS, COLS = len(rooms), len(rooms[0])

        # get all the gates in the dq
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    dq.append((r, c))
                    seen.add((r, c))
        
        while dq:
            k = len(dq)
            distance += 1
            for _ in range(k):
                r, c = dq.popleft()
                for row, col in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                    if ((0 <= row < NROWS) and
                        (0 <= col < NCOLS) and
                        ((row, col) not in seen) and
                        (rooms[row][col] == 2147483647)):
                            rooms[row][col] = distance
                            dq.append((row, col))
```

TC: O(m * n)

SC: O(m * n)