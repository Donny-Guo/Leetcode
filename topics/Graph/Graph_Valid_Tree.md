# Graph Valid Tree

https://leetcode.com/problems/graph-valid-tree/description/

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer n and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` *if the edges of the given graph make up a valid tree, and* `false` *otherwise*.

 

**Example 1:**

![img](./assets/tree1-graph.jpg)

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2:**

![img](./assets/tree2-graph.jpg)

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

 

**Constraints:**

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- There are no self-loops or repeated edges.



**Reflections**:

- the definition of tree: connected, acyclic, undirected graph
- Another feature of tree: there's only one path between two nodes -> no need to remove node from visited during cycle detection
- use visited (hash set) to detect cycle, also check if all the nodes are connected
- since we only need to traverse the graph, both bfs/dfs work



## Solution: dfs

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = {i: [] for i in range(n)}
        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)
        cycle = set()

        def dfs(root, prevNode) -> bool:
            # base case
            if root in cycle: return False

            # general case:
            cycle.add(root)
            for neighbor in mp[root]:
                if neighbor == prevNode: continue
                if not dfs(neighbor, root): return False

            return True
        
        if not dfs(0, -1): return False
```

TC: O(V+E)

SC: O(V+E)



## Solution: bfs:

```python
from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # mp
        mp = {i: [] for i in range(n)}
        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)
        # visited:
        visited = set()
        # queue
        dq = deque()
        # add [0, -1] to queue:
        dq.append((0, -1))
        visited.add(0)
        # while dq not empty:
        while dq:
            # popleft
            curr, prev = dq.popleft()
            # for each neighbor:
            for neighbor in mp[curr]:
                # if is prev: continue
                if neighbor == prev: continue
                # if in visited: return False
                if neighbor in visited: return False
                # else: append to dq
                else:
                    visited.add(neighbor)
                    dq.append((neighbor, curr))
        return len(visited) == n
```

TC: O(V+E)

SC: O(V+E)