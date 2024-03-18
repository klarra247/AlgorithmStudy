from heapq import heappop, heappush

num = int(input())

heap = []
answer = []
for _ in range(num):
    inp = int(input())
    if inp == 0:
        if heap:
            answer.append(str(heappop(heap)))
        else:
            answer.append(str(0))
    else:
        heappush(heap, inp)

print('\n'.join(answer))
