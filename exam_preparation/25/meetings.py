'''Задача о встречах. Нужно сходить на как можно больше'''

def max_meetings(meetings):
    if len(meetings) == 0:
        return []
    sort_meet = sorted(meetings, key=lambda x: x[1])
    selected = [sort_meet[0]]
    last_end = sort_meet[0][1]
    for start, end in sort_meet[1:]:
        if start > last_end:
            selected.append((start, end))
            last_end = end
    return selected

meetings = [
        (9, 11),   
        (10, 12),  
        (11, 13),  
        (12, 14),  
        (13, 15),  
        (14, 16),  
    ]
print(max_meetings(meetings))
