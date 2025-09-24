'''

One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests.
Participants are usually offered several problems during programming contests.
Long before the start the friends decided that they will implement a problem if at least two of them are sure about the solution.
Otherwise, the friends won't write the problem's solution.

This contest offers n problems to the participants. For each problem we know, which friend is sure about the solution.
Help the friends find the number of problems for which they will write a solution.

Input

The first input line contains a single integer n (1 ≤ n ≤ 1000) — the number of problems in the contest.
Then n lines contain three integers each, each integer is either 0 or 1.
If the first number in the line equals 1, then Petya is sure about the problem's solution, otherwise he isn't sure.
The second number shows Vasya's view on the solution, the third number shows Tonya's view.
The numbers on the lines are separated by spaces.

Output

Print a single integer — the number of problems the friends will implement on the contest.

'''



# def contest_solver (n):
#     num1 = 0
#     num2 = 0
#     num3 = 0
#     i = 0
#     count = 0
#     while i < n:
#         num1 = int(input())
#         num2 = int(input())
#         num3 = int(input())
#         sum = num1 + num2 + num3
#         if (sum > 1):
#             count += 1
#         i += 1
#     return count
#
#
#
# # input Number of Contest
# num_of_contest = int(input("Enter Number of Contest:"))
#
# result = contest_solver(num_of_contest)
# print("Contest Solved: ", result)




#  ChatGTP Code

n = int(input())
count = 0
for _ in range(n):
    p, v, t = map(int, input().split())
    if p + v + t >= 2:
        count += 1
print(count)