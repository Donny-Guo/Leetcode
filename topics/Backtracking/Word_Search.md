# Word Search

https://leetcode.com/problems/word-search/description/

Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

**Example 1:**

![img](./assets/word2.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2:**

![img](./assets/word-1.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:**

![img](./assets/word3.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

 

**Constraints:**

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

 

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?



## Solution

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        nrow, ncol = len(board), len(board[0])

        def backtrack(row, col, i):
            if i == len(word): return True
            # base case
            if 0 <= row < nrow and 0 <= col < ncol and (row, col) not in visited and i < len(word) and board[row][col] == word[i]:
                visited.add((row, col))
                # explore four directions
                for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                    if backtrack(r, c, i+1): return True
                visited.remove((row, col))
                return False
            return False
        
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0): return True
        return False
```

TC: O(*N*⋅3*L*) where *N* is the number of cells in the board and *L* is the length of the word to be matched

SC: O(L)