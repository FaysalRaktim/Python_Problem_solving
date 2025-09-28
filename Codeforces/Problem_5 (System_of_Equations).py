'''

A. System of Equations

Furik loves math lessons very much, so he doesn't attend them, unlike Rubik. But now Furik wants to get a good mark
for math. For that Ms. Ivanova, his math teacher, gave him a new task. Furik solved the task immediately. Can you?

You are given a system of equations:


You should count, how many there are pairs of integers (ab) (0 ≤ a, b) which satisfy the system.

Input
A single line contains two integers n, m (1 ≤ n, m ≤ 1000) — the parameters of the system.
The numbers on the line are separated by a space.

Output
On a single line print the answer to the problem.

'''

n, m = map(int, input().split())
count = 0

for a in range(n + 1):
    for b in range(m + 1):
        if a ** 2 + b == n and a + b ** 2 == m:
            count += 1

print(count)
