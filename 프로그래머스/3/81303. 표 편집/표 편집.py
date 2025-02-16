# def solution(n, k, cmd):
#     # n = 행의 개수 k = 처음에 선택된 행의 위치 cmd = 명령어 문자열
#     answer = ['O'] * n
#     stack = []
#     deleted = set()
    
# # '0X00X00X'
#     for action in cmd:
#         if action[0] == 'D':
#             x = int(action.split()[1])
#             while x > 0:
#                 k += 1
#                 if k not in deleted:
#                     x -= 1
                
#         elif action[0] ==  'U':
#             x = int(action.split()[1])
#             while x > 0:
#                 k -= 1
#                 if k not in deleted:
#                     x -= 1
                
#         elif action[0] == 'C':
#             answer[k] = 'X'
#             stack.append(k)
#             deleted.add(k)
            
#             a = k
#             while a < n and a in deleted:
#                 a += 1
#             if a < n:
#                 k = a
#             else:
#                 a = k
#                 while a in deleted:
#                     a -= 1
#                 k = a            
            
#         elif action[0] == 'Z':
#             idx = stack.pop()
#             deleted.remove(idx)
#             answer[idx] = 'O'
            
#     return ''.join(answer)

def solution(n, k, cmd):
    answer = ['O'] * n
    stack = []
    linked_list = {i: [i-1, i+1] for i in range(n)}
    linked_list[0] = [-1, 1]
    linked_list[n-1] = [n-2, -1]
    
    for action in cmd:
        if action[0] == 'D':
            x = int(action.split()[1])
            for _ in range(x):
                k = linked_list[k][1]
                
        elif action[0] == 'U':
            x = int(action.split()[1])
            for _ in range(x):
                k = linked_list[k][0]
                
        elif action[0] == 'C':
            answer[k] = 'X'
            prev, next = linked_list[k]
            stack.append([k, prev, next])
            
            if prev != -1:
                linked_list[prev][1] = next
            if next != -1:
                linked_list[next][0] = prev
                k = next
            else:
                k = prev
                
        elif action[0] == 'Z':
            idx, prev, next = stack.pop()
            answer[idx] = 'O'
            
            if prev != -1:
                linked_list[prev][1] = idx
            if next != -1:
                linked_list[next][0] = idx
            linked_list[idx] = [prev, next]
            
    return ''.join(answer)