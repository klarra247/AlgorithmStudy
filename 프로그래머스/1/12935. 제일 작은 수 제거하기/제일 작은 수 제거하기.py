def solution(arr):

    min_num = min(arr)
    for index, number in enumerate(arr):
        if number == min_num:
            if arr[:index] + arr[index+1:] == []:
                return [-1]
            else:
                return arr[:index] + arr[index+1:]
