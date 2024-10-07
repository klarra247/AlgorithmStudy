def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if num_of_factors(num) % 2 == 0:
            answer += num
        else:
            answer -= num
            
    return answer

def num_of_factors(number):
    factors = 0
    for i in range(1, number + 1):
        if number % i == 0:
            factors += 1
            
    print(factors)
    return factors
        
