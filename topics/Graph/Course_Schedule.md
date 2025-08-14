# Course Schedule

https://leetcode.com/problems/course-schedule/description/

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

 

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:**

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

 

**Constraints:**

- `1 <= numCourses <= 2000`

- `0 <= prerequisites.length <= 5000`

- `prerequisites[i].length == 2`

- `0 <= ai, bi < numCourses`

- All the pairs prerequisites[i] are **unique**.

  

**Reflections**:

- not possible: there's a cycle in the prerequisite graph
- don't forget the graph could be disconnected



## Solution: DFS with cycle detection

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initial map: key=course, value=[list of prerequisites]
        mp = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            mp[a].append(b)
        
        visited = set()
        def dfs(course):
            # base case
            if course in visited: # if there's a loop
                return False
            if mp[course] == []: return True

            # general case:
            visited.add(course)
            # require to clear all prerequisites
            for preq in mp[course]:
                if not dfs(preq): 
                    return False
        
            # backtrack cleanup: course is no longer on the path of checking cycle
            visited.remove(course)
            mp[course] = [] # this course can take
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
```

- Time complexity: O(V+E)
- Space complexity: O(V+E)

Where V is the number of courses and E is the number of prerequisites.



## Solution: topological sort

Tolopogical sort is an algorithm that takes in a directed graph and return a list of node in the order that the node appears before all the nodes it points to. https://www.interviewcake.com/concept/python3/topological-sort

We'll use the strategy we outlined above:

1. Identify a node with no incoming edges.
2. Add that node to the ordering.
3. Remove it from the graph.
4. Repeat.

We'll keep looping until there aren't any more nodes with indegree zero. This could happen for two reasons:

- There are no nodes left. We've taken all of them out of the graph and added them to the topological ordering.
- There are some nodes left, but they all have incoming edges. This means the graph has a cycle, and no topological ordering exists.

```python
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        mp = {i: [] for i in range(numCourses)}

        for crs, preq in prerequisites:
            mp[preq].append(crs)
            inDegree[crs] += 1
        
        dq = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                dq.append(i)
        
        count = 0
        while dq:
            curr = dq.popleft()
            count += 1
            for crs in mp[curr]:
                inDegree[crs] -= 1
                if inDegree[crs] == 0:
                    dq.append(crs)
        
        return count == numCourses
```

- Time complexity: O(V+E)
- Space complexity: O(V+E)

Where V is the number of courses and E is the number of prerequisites.