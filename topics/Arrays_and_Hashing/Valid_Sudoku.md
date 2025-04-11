# Valid Sudoku

https://leetcode.com/problems/valid-sudoku/description/

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

 

**Example 1:**

![img](./assets/250px-Sudoku-by-L2G-20050714.svg.png)

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2:**

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

 

**Constraints:**

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.



**Reflections**:

1. there are many ways to detect duplicate, set is a pretty elegant solution compared to array
2. use dict together with set can do one pass
3. locate boxes by using (row//3, col//3) as dict key



## Solution 1: 

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(block: List[str]) -> bool:
            count = [0] * 10
            for s in block:
                if s == '.': continue
                count[int(s)] += 1
                if count[int(s)] > 1:
                    return False
            return True
        
        # for row:
        for row in board:
            if isValid(row): continue
            return False
        
        # for col:
        for col in range(9):
            col_str = []
            for row in range(9):
                col_str.append(board[row][col])
            if isValid(col_str): continue
            return False
        
        # for subbox
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                block_str = []
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        block_str.append(board[i][j])
                if isValid(block_str): continue
                return False

        return True
```

TC: O(n^2)

SC: O(n) only for one block



## Solution 2: Dict + set

```python
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': continue
                elif (board[r][c] in row[r]) or \
                     (board[r][c] in col[c]) or \
                     (board[r][c] in box[(r//3, c//3)]):
                    return False
                else:
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    box[(r//3, c//3)].add(board[r][c])
        
        return True
```

TC: O(n^2)

SC: O(n^2) -> one set is O(n), n sets is O(n^2)