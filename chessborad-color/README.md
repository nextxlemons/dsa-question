# Chessboard Cell Color

**Difficulty:** Easy
**Topics:** Math, String Parsing
**Platform/Source:** Unstop

## Problem Statement

Given a chessboard represented as a 2D cartesian plane (columns a–h on the x-axis,
rows 1–8 on the y-axis), determine whether a given cell is **White** or **Black**.

### Input Format
- A single string `s` of length 2 (e.g. `"b2"`).

### Output Format
- `"White"` or `"Black"`.

### Constraints
- `|s| = 2`

### Sample Input/Output

| Input | Output | Explanation |
|-------|--------|-------------|
| `b2`  | Black  | Sum of column index (2) + row (2) = 4, even → Black |
| `a1`  | Black  | Sum of column index (1) + row (1) = 2, even → Black |

## Approach

- Map column letters `a-h` to indices `1-8`.
- Convert row character to integer.
- If `(col_index + row) % 2 == 0` → the cell is Black, else White.

## Complexity
- **Time:** O(1) (constant-size board, max 8 iterations to find column index)
- **Space:** O(1)

## Code
See [`solution.py`](./solution.py)