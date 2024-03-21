from itertools import combinations

N, M = map(int, input().split())    # N장의 카드, 합은 M을 넘지 말아야

cards = list(map(int, input().split()))

combs = combinations(cards, 3)
res = 0

for comb in combs:
    if sum(comb) <= M:
        res = max(res, sum(comb))

print(res)