def solution(s):
    if len(list(s)) % 2 == 0:
        index = len(list(s)) // 2
        return ''.join(list(s)[index-1:index+1])
    else: 
        index = (len(list(s)) - 1) // 2
        return list(s)[index]
