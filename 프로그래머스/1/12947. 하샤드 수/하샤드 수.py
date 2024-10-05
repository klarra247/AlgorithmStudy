def solution(x):
    nums = list(str(x))
    sumx = sum(list(map(int, nums)))
    
    
    if x % sumx == 0:
        return True
    else:
        return False
