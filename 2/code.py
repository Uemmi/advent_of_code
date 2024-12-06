
# first question
num_safe = 0
with open('/Users/ummi/Documents/Traineeship/advent_of_code/2/input.txt', 'r') as file:
    
    for line in file:
        report = list(line.strip().split(" "))
        increasing = False
        is_safe = True
        if int(report[1]) - int(report[0]) > 0:
            increasing = True
        removed = 0    
        for level_i in range(1, len(report)):
            curr = int(report[level_i])
            old = int(report[level_i-1])
            diff = curr - old
            if (diff > 0) and (not increasing): 
                is_safe = False
                break
            if (diff < 0) and increasing: 
                is_safe = False
                break
            if (abs(diff) > 3) or (abs(diff) < 1):
                is_safe = False
                break
        if is_safe:
            num_safe += 1
print(num_safe)     

# second question
def check_levels(first, second, increasing):
    diff = second - first
    if (diff > 0) and (not increasing): 
        return False
    if (diff < 0) and increasing: 
        return False
    if (abs(diff) > 3) or (abs(diff) < 1):
        return False
    return True

def check_if_first_entry_causes_violations(report):
    remove = None
    increasing_0 = int(report[1]) - int(report[0]) > 0
    increasing_1 = int(report[2]) - int(report[1]) > 0
    increasing_2 = int(report[3]) - int(report[2]) > 0

    if increasing_1 == increasing_2 and increasing_0 != increasing_1:
        remove = 0
    elif increasing_0 != increasing_1 and abs(int(report[0]) - int(report[2])) < 3 and abs(int(report[0]) - int(report[2])) > 0:
        remove = 1
    return remove          

def check_list(report):
    increasing = False
    is_safe = True
    if int(report[1]) - int(report[0]) > 0:
        increasing = True
    for level_i in range(1, len(report)):
        curr = int(report[level_i])
        old = int(report[level_i-1])
        diff = curr - old
        if (diff > 0) and (not increasing): 
            is_safe = False
            break
        if (diff < 0) and increasing: 
            is_safe = False
            break
        if (abs(diff) > 3) or (abs(diff) < 1):
            is_safe = False
            break
    return is_safe

num_safe = 0
with open('/Users/ummi/Documents/Traineeship/advent_of_code/2/input.txt', 'r') as file:
    
    for line in file:
        removed = 0
        report = list(line.strip().split(" "))
        level_i = 1
        remove = check_if_first_entry_causes_violations(report)
        if remove != None:
            print(remove)
            print(report)
            report.pop(remove)
            removed = 1     
        increasing = int(report[1]) - int(report[0]) > 0
        curr = level_i
        prev = level_i-1
        is_safe = True
        while level_i < len(report):
            if not check_levels(int(report[prev]), int(report[curr]), increasing):
                if removed:
                    is_safe = False
                    break
                else:
                    # remove curr
                    if curr == len(report)-1:
                        is_safe = True
                        break
                    if curr < len(report)-2 and check_levels(int(report[prev]), int(report[curr+1]), increasing):
                        if check_levels(int(report[curr+1]), int(report[curr+2]), increasing):
                            removed = 1
                            level_i += 2
                            curr = level_i
                            prev = level_i-1

                    # remove prev    
                    elif check_levels(int(report[prev-1]), int(report[curr]), increasing):   
                        removed = 1
                        level_i += 1
                        curr = level_i
                        prev = level_i-1
                    else:
                        #print(report)
                        is_safe = False
                        break
            else:
                level_i += 1
                curr = level_i
                prev = level_i-1         
        if is_safe:
            num_safe += 1            

print(num_safe)   

# O(n^2) complexity
# def check_levels(first, second, increasing):
#     diff = second - first
#     if (diff > 0 and not increasing) or (diff < 0 and increasing):
#         return False
#     if abs(diff) < 1 or abs(diff) > 3:
#         return False
#     return True


# def check_list(report):
#     increasing = int(report[1]) - int(report[0]) > 0
#     for i in range(1, len(report)):
#         if not check_levels(int(report[i - 1]), int(report[i]), increasing):
#             return False
#     return True


# num_safe = 0
# with open('/Users/ummi/Documents/Traineeship/advent_of_code/2/input.txt', 'r') as file:
#     for line in file:
#         report = list(map(int, line.strip().split()))
#         if check_list(report):
#             num_safe += 1
#             continue

#         # Try removing one level to make it safe
#         for i in range(len(report)):
#             new_report = report[:i] + report[i + 1:]  # Remove one level
#             if check_list(new_report):
#                 num_safe += 1
#                 break

# print(num_safe)
