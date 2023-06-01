n = int(input().split(maxsplit=0)[0])
a = d = 0
s = input().upper()

for ch in s:
    if ch == 'A':
        a += 1
    elif ch == 'D':
        d += 1

if a > d:
    print('Anton')
elif d > a:
    print('Danik')
else:
    print('Friendship')

