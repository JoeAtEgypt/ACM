n = int(input().split(maxsplit=0)[0])
contest = [input().split(maxsplit=3) for _ in range(n)]

s = 0

for problem in contest:
    if problem.count("1") >= 2:
        s += 1

print(s)


