n, m = map(int, input().strip().split(' '))
answer = ""
for i in range(m):
    answer += '*' * n + '\n'
print(answer)
