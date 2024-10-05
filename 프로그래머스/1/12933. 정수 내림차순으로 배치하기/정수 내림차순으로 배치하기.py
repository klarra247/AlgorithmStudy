def solution(n):
    nums = list(str(n))
    nums.sort(reverse = True)
    return int(''.join(nums))