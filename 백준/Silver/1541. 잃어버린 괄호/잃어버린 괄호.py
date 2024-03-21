equation = input()
sign = ['-', '+']
stack = []
res = 0
neg = False
for val in equation:
    if val in sign:            
        if neg:
            res -= int(''.join(stack))
        else:
            res += int(''.join(stack))
        if val == '-':
            neg = True
        stack = []
    elif val == '0':
        if stack:
            stack.append(val)
    else:
        stack.append(val)
if stack:
    if neg:
        res -= int(''.join(stack))
        if val == '-':
            neg = False
    else:
        res += int(''.join(stack))
        if val == '-':
            neg = True

print(res)