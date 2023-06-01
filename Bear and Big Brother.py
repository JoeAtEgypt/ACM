a, b = list(map(int, input().split(maxsplit=2)[:2]))
years = 0

while True:
    if a > b:
        print(years)
        break
    else:
        a, b = a*3, b*2
        years += 1
