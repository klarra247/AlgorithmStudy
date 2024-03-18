# 큐의 크기 N, 개수 M
from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

# 채워진 deque 생성
nums = deque(range(1,n+1))
count = 0

for target in targets:
    moved_left = 0
    while nums[0] != target:
        nums.append(nums.popleft())
        moved_left += 1
    count += min(moved_left, n - moved_left)
    nums.popleft()
    n -= 1
    
print(count)
