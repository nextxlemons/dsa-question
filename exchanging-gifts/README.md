# Exchangeing Gifts

**Difficulty:** Easy
**Topics:** Math, String Parsing
**Platform/Source:** Unstop

## Problem Statement

The royal family exchanges gifts at Christmas, where the youngest member receives gifts from everyone but doesn't give any gifts. Given the data for all the exchanged gifts among the family members, you need to identify the youngest member, who is the one receiving gifts from everyone but not giving any.

**Note :** A family member does not give more than one gift to the same member.

### Input Format
- The first line of the input contains two integers n and m denoting the number of family members and the number of gifts that were exchanged.

### Output Format
- Print a single integer, the number that represents the youngest member of the family.


### Constraints
- `1 <= n <= 104

0 <= m <= 105

1 <= ai, bi, <= n`

### Sample Input/Output

| Input | Output | Explanation |
|-------|--------|-------------|
| `2 1
1 2`  | 2  | Family member 1 gave a gift to family member 2. Now, we can see that 2 did not give any gift to anyone but received a gift from all other members (member 1). Hence, 2 is the youngest member.
Sample Testcase 1 |
| `3 2
1 3
2 3`  | 3  | Explanation
We can see that 3 received gifts from 1 and 2 but did not give any gifts to anyone. Therefore, 3 must be the youngest member.k |

## Approach



## Complexity
- **Time:** O(1) (constant-size board, max 8 iterations to find column index)
- **Space:** O(1)

## Code
See [`solution.py`](./solution.py)

