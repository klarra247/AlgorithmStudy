N, K = map(int, input().split())
coins = []

for _ in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)

result = 0


while coins:
    coin = coins.pop()
    result += K // coin
    K = K % coin

    if K == 0:
        break


print(result)
