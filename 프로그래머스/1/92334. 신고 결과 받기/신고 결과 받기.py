def solution(id_list, report, k):
    answer = []
    numbers = {}
    reports = {}
    id_dict = {}
    for id in id_list:
        id_dict[id] = 0
        
    for i in report:
        reporter, reportee = i.split()
        
        if reportee in numbers:
            if reporter not in reports[reportee]:
                numbers[reportee] += 1
                reports[reportee].add(reporter)
        else: 
            reports[reportee] = {reporter}
            numbers[reportee] = 1
    
    for key, val in numbers.items():
        if val >= k:
            for reporter in reports[key]:
                id_dict[reporter] += 1
    
    return list(id_dict.values())
                
            
        
    print(numbers)
    print(reports)