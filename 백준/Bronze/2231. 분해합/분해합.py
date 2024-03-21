N = int(input())

const = 0
ssum = 0
while const <= N:
    ssum = sum(list(map(int, str(const))))
    if const + ssum == N:
        print(const)
        break
    else:
        const += 1

if const > N:
    print(0)