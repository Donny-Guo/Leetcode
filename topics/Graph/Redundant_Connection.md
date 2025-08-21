# Redundant Connection

https://leetcode.com/problems/redundant-connection/description/

In this problem, a tree is an **undirected graph** that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two **different** vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

Return *an edge that can be removed so that the resulting graph is a tree of* `n` *nodes*. If there are multiple answers, return the answer that occurs last in the input.

 

**Example 1:**

![img](./assets/reduntant1-1-graph.jpg)

```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

**Example 2:**

![img](./assets/reduntant1-2-graph.jpg)

```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

 

**Constraints:**

- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= ai < bi <= edges.length`
- `ai != bi`
- There are no repeated edges.
- The given graph is connected.



**reflections**:

- perfect problem for union find: undirected graph, and detect cycle



## Solution: Union-Find

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = list(range(n+1))
        rank = [1] * (n+1)

        def find(node):
            curr = node
            while curr != par[curr]:
                par[curr] = par[par[curr]]
                curr = par[curr]
            return curr
        
        def union(n1, n2) -> bool:
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True
        
        for a, b in edges:
            if not union(a, b): return [a, b]
```

TC: O(V+E)

SC: O(V)