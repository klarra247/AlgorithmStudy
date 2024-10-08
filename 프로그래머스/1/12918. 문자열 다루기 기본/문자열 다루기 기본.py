def solution(s):
    if len(s) == 4 or len(s) == 6:
        for char in s:
            if not char.isdigit():
                return False
        return True
    else:
        return False
    answer = True
    return answer