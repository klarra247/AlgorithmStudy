def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index
            
        stack.append(i)
    
    while stack:
        i = stack.pop()
        answer[i] = len(prices) - i - 1
        
    return answer
