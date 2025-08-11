# Pacific Atlantic Water Flow

https://leetcode.com/problems/pacific-atlantic-water-flow/description/

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return *a **2D list** of grid coordinates* `result` *where* `result[i] = [ri, ci]` *denotes that rain water can flow from cell* `(ri, ci)` *to **both** the Pacific and Atlantic oceans*.

 

**Example 1:**

![img](./assets/waterflow-grid.jpg)

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
```

**Example 2:**

```
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
```

 

**Constraints:**

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 105`



**Reflections**:

- start traversal from ocean
- both dfs/bfs work since it does not require shortest path



## Solution: dfs

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(r, c, visited, prevHeight):
            if ((0 <= r < ROWS) and
                (0 <= c < COLS) and 
                ((r, c) not in visited) and 
                (heights[r][c] >= prevHeight)):

                visited.add((r, c))
                for row, col in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                    dfs(row, col, visited, heights[r][c])
        
        # for rows:
        for r in range(ROWS):
            dfs(r, 0, pacific, 0)
            dfs(r, COLS-1, atlantic, 0)
        
        # for cols:
        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS-1, c, atlantic, 0)
        
        res = []
        # for all cels
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res
```

TC: O(m * n)

SC: O(m * n)



## Solution: bfs

```python
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific, atlantic = set(), set()
        q_pacific, q_atlantic = deque(), deque()
        ROWS, COLS = len(heights), len(heights[0])
        # start pacific
        for c in range(COLS):
            q_pacific.append((0, c))
            pacific.add((0, c))
        for r in range(1, ROWS):
            q_pacific.append((r, 0))
            pacific.add((r, 0))
        # start atlantic
        for r in range(ROWS):
            q_atlantic.append((r, COLS-1))
            atlantic.add((r, COLS-1))
        for c in range(COLS-1):
            q_atlantic.append((ROWS-1, c))
            atlantic.add((ROWS-1, c))

        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()
                for new_r, new_c in [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]:
                    if ((0 <= new_r < ROWS) and 
                        (0 <= new_c < COLS) and 
                        ((new_r, new_c) not in visited) and 
                        (heights[new_r][new_c] >= heights[row][col])):
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))

        bfs(q_atlantic, atlantic)
        bfs(q_pacific, pacific)
       
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
```

TC: O(m * n)

SC: O(m * n)