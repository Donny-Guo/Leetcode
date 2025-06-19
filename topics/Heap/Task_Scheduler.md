# Task Scheduler

https://leetcode.com/problems/task-scheduler/description/

You are given an array of CPU `tasks`, each labeled with a letter from A to Z, and a number `n`. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of **at least** `n` intervals between two tasks with the same label.

Return the **minimum** number of CPU intervals required to complete all tasks.

 

**Example 1:**

**Input:** tasks = ["A","A","A","B","B","B"], n = 2

**Output:** 8

**Explanation:** A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

**Example 2:**

**Input:** tasks = ["A","C","A","B","D","B"], n = 1

**Output:** 6

**Explanation:** A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

**Example 3:**

**Input:** tasks = ["A","A","A", "B","B","B"], n = 3

**Output:** 10

**Explanation:** A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

**Constraints:**

- `1 <= tasks.length <= 104`
- `tasks[i]` is an uppercase English letter.
- `0 <= n <= 100`



## Solution: MaxHeap

```python
from collections import defaultdict, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        heap = [(-count) for count in freq.values()]
        heapq.heapify(heap)
        queue = deque([])
        clock = 0

        while heap or queue:
            if heap:
                negativeCount = heapq.heappop(heap)
                if negativeCount < -1:
                    negativeCount += 1
                    queue.append((clock + n + 1, negativeCount))

            clock += 1
            if queue and queue[0][0] == clock:
                _, negativeCount = queue.popleft()
                heapq.heappush(heap, (negativeCount))
        
        return clock
```

TC: O(n) since only contains upper English letter

SC: O(26) = O(1)