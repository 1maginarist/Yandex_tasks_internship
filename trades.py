n = int(input())
prices = list(map(int, input().split()))

profits = []
buy_day = -1

for i in range(n - 1):
    if prices[i] < prices[i + 1]:
        if buy_day == -1 or prices[i] < prices[buy_day]:
            buy_day = i

    elif prices[i] > prices[i + 1]:
        if buy_day != -1 and prices[i] > prices[buy_day]:
            profits.append((buy_day + 1, i + 1))
            buy_day = -1

if buy_day != -1 and prices[n - 1] > prices[buy_day]:
    profits.append((buy_day + 1, n))

print(len(profits))
for p in profits:
    print(p[0], p[1])