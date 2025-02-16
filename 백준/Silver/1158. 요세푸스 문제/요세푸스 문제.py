from collections import deque

N, K = map(int, input().split())
nums = deque(range(1,N+1))
result = []
while nums:
    for _ in range(K-1):
        nums.append(nums.popleft())
    result.append(str(nums.popleft()))

print("<"+', '.join(result)+">")