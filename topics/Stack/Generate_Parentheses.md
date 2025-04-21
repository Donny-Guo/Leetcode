# Generate Parentheses

https://leetcode.com/problems/generate-parentheses/description/

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

 

**Example 1:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**

```
Input: n = 1
Output: ["()"]
```

 

**Constraints:**

- `1 <= n <= 8`



**Reflections**:

1. use backtracking (explore all possible solutions and undo after each exploration: depth-first search with undo)



## Solution

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def helper(openCnt, closeCnt):
            # base case
            if openCnt == n and closeCnt == n:
                res.append(''.join(stack))
                return
            
            # general case
            if (openCnt < n):
                stack.append('(')
                helper(openCnt+1, closeCnt)
                stack.pop(-1)
            
            if (openCnt > closeCnt):
                stack.append(')')
                helper(openCnt, closeCnt + 1)
                stack.pop(-1)
        
        helper(0, 0)
        return res
```

