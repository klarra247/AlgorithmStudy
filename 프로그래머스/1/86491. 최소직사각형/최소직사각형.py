def solution(sizes):
    arranged_sizes = []
    maxwidth = 0
    maxheight = 0
    for width, height in sizes:
        arranged_sizes.append([max(width, height), min(width, height)])
        if max(width, height) > maxwidth:
            maxwidth = max(width, height)
        if min(width, height) > maxheight:
            maxheight = min(width, height)
    
    return maxwidth * maxheight