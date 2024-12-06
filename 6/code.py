import copy

# part 1
with open('/Users/ummi/Documents/Traineeship/advent_of_code/6/input.txt', 'r') as file:
    raw_matrix = [list(line.strip()) for line in file]

directions = {
              "^": [-1,0],
              ">": [0,1],
              "v": [1, 0],
              "<": [0,-1]
              }

curr_pos = None
curr_dir = None
matrix=copy.deepcopy(raw_matrix)
rows = len(matrix)
columns = len(matrix[0])

for row in range(rows):
    if curr_dir:
        break
    for column in range(columns):
        if curr_dir:
            break
        if matrix[row][column] == "^":
            curr_pos = [row, column]
            curr_dir = "^"
        elif matrix[row][column]  == ">":
            curr_pos = [row, column]
            curr_dir = ">"
        elif matrix[row][column]  == "v":
            curr_pos = [row, column]
            curr_dir = "v"
        elif matrix[row][column]  == "<":
            curr_pos = [row, column]
            curr_dir = "<"                
walk = [curr_pos]
walked = 1
matrix[curr_pos[0]][curr_pos[1]] = curr_dir
starting_pos=curr_pos
while True:
    next_pos = [curr_pos[0]+directions[curr_dir][0], curr_pos[1]+directions[curr_dir][1]]
    if next_pos[0]>=rows or next_pos[1]>=columns or next_pos[0]<0 or next_pos[1]<0 :
        break
    if matrix[next_pos[0]][next_pos[1]] == "#":
        if curr_dir == "^":
            curr_dir = ">"
        elif curr_dir == ">":
            curr_dir = "v"
        elif curr_dir == "v":
            curr_dir = "<"
        elif curr_dir == "<":
            curr_dir = "^"    
    else:
        curr_pos = next_pos
        walk.append(curr_pos)
        if matrix[next_pos[0]][next_pos[1]] not in directions.keys():
            walked += 1
            matrix[next_pos[0]][next_pos[1]] = curr_dir  

print(walked)

# part 2

def turn(dir):
    if dir == "^":
        curr_dir = ">"
    elif dir == ">":
        curr_dir = "v"
    elif dir == "v":
        curr_dir = "<"
    elif dir == "<":
        curr_dir = "^"   
    return curr_dir    

def simulate_obstacle(pos, dir, initial_matrix):
    matrix = copy.deepcopy(initial_matrix)
    curr_pos = pos
    curr_dir = dir
    while True:
        next_pos = [curr_pos[0]+directions[curr_dir][0], curr_pos[1]+directions[curr_dir][1]]
        if next_pos[0]>=rows or next_pos[1]>=columns or next_pos[0]<0 or next_pos[1]<0 :
            return False
        if matrix[next_pos[0]][next_pos[1]] == curr_dir:
            return True
        if matrix[next_pos[0]][next_pos[1]] == "#":
            if curr_dir == "^":
                curr_dir = ">"
            elif curr_dir == ">":
                curr_dir = "v"
            elif curr_dir == "v":
                curr_dir = "<"
            elif curr_dir == "<":
                curr_dir = "^"    
        else:
            curr_pos = next_pos
            if matrix[next_pos[0]][next_pos[1]] not in directions.keys():
                matrix[next_pos[0]][next_pos[1]] = curr_dir  

initial_state = copy.deepcopy(raw_matrix)
loops = []

for row, column in walk:
        initial_state[row][column] = matrix[row][column]
        if [row, column] == starting_pos:
            continue
        if initial_state[row][column] in directions.keys():
            row_start = row - directions[initial_state[row][column]][0]
            column_start = column - directions[initial_state[row][column]][1]
            dir = turn(initial_state[row][column])
            initial_test_state = copy.deepcopy(initial_state)
            initial_test_state[row][column] = "O"
            loop = simulate_obstacle([row_start, column_start], dir, initial_test_state)
            if loop:
                loops.append([row,column])

def count_unique_lists_in_list_of_lists(lst):
    """
    Count the number of unique lists in a list of lists.
    """
    # Convert lists to tuples (since lists are unhashable) and use a set for uniqueness
    unique_tuples = set(tuple(sublist) for sublist in lst)
    # Return the count of unique lists
    return len(unique_tuples)

print(count_unique_lists_in_list_of_lists(loops))






