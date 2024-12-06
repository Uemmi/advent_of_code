# part 1
import numpy as np

file_path = '/Users/ummi/Documents/Traineeship/advent_of_code/4/input.txt'

with open(file_path, 'r') as file:
    data = [list(line.strip()) for line in file]

input = np.array(data)

# forward pass
current_words = {"right": [], "down": [], "diagonal_1": [],  "diagonal_2": []}
word = ["X", "M", "A", "S"]
row = 0
count = 0
while row < len(input):
    column = 0
    current_words = {"right": [input[row, column]], "down": [input[row, column]], "diagonal_1": [input[row, column]],  "diagonal_2": [input[row, column]]}
    while column < len(input[0]):
        for i in range(4):
            # right
            if len(current_words["right"]) < 4:
                if current_words["right"] == word[:len(current_words["right"])]:
                    if column+len(current_words["right"]) < len(input[0]):
                        current_words["right"].append(input[row, column+len(current_words["right"])])             
            else:               
                if current_words["right"] == word:
                    count +=1
            # down
            if len(current_words["down"]) < 4:
                if current_words["down"] == word[:len(current_words["down"])]:
                    if row+len(current_words["down"]) < len(input):
                        current_words["down"].append(input[row+len(current_words["down"]), column])
            else:                
                if current_words["down"] == word:
                    print(current_words["down"], row, column)
                    count +=1
            # diagonal1
            if len(current_words["diagonal_1"]) < 4:
                if current_words["diagonal_1"] == word[:len(current_words["diagonal_1"])]:
                    if row+len(current_words["diagonal_1"]) < len(input) and column+len(current_words["diagonal_1"]) < len(input[0]):
                        current_words["diagonal_1"].append(input[row+len(current_words["diagonal_1"]), column+len(current_words["diagonal_1"])])       
            else:                
                if current_words["diagonal_1"] == word:
                    count +=1
            # diagonal2
            if len(current_words["diagonal_2"]) < 4:
                if current_words["diagonal_2"] == word[:len(current_words["diagonal_2"])]:
                    if row-len(current_words["diagonal_2"]) >= 0 and column+len(current_words["diagonal_2"]) < len(input[0]):
                        current_words["diagonal_2"].append(input[row-len(current_words["diagonal_2"]) , column+len(current_words["diagonal_2"])])      
            else:                
                if current_words["diagonal_2"] == word:
                    count +=1  
        column += 1
        if column < len(input[0]):
            current_words = {"right": [input[row, column]], "down": [input[row, column]], "diagonal_1": [input[row, column]],  "diagonal_2": [input[row, column]]}
    row += 1  
    if row < len(input) and column < len(input[0]):
        current_words = {"right": [input[row, column]], "down": [input[row, column]], "diagonal_1": [input[row, column]],  "diagonal_2": [input[row, column]]}


print(count)    
# backward pass
current_words = {"right": [], "down": [], "diagonal_1": [],  "diagonal_2": []}
word = ["X", "M", "A", "S"]
row = len(input)-1
while row >= 0:
    column = len(input[0])-1
    current_words = {"right": [input[row, column]], "down": [input[row, column]], "diagonal_1": [input[row, column]],  "diagonal_2": [input[row, column]]}
    while column >=0:
        for i in range(4):
            # right
            if len(current_words["right"]) < 4:
                if current_words["right"] == word[:len(current_words["right"])]:
                    if column-len(current_words["right"]) >= 0:
                        current_words["right"].append(input[row, column-len(current_words["right"])])     
            else:                
                if current_words["right"] == word:
                    count +=1
            # down
            if len(current_words["down"]) < 4:
                if current_words["down"] == word[:len(current_words["down"])]:
                    if row-len(current_words["down"]) >= 0:
                        current_words["down"].append(input[row-len(current_words["down"]) , column])
            else:                 
                if current_words["down"] == word:
                    count +=1
            # diagonal1
            if len(current_words["diagonal_1"]) < 4:
                if current_words["diagonal_1"] == word[:len(current_words["diagonal_1"])]:
                    if row-len(current_words["diagonal_1"]) >=0 and column-len(current_words["diagonal_1"]) >=0:
                        current_words["diagonal_1"].append(input[row-len(current_words["diagonal_1"]), column-len(current_words["diagonal_1"])])   
            else:                 
                if current_words["diagonal_1"] == word:
                    count +=1
            # diagonal2
            if len(current_words["diagonal_2"]) < 4:
                if current_words["diagonal_2"] == word[:len(current_words["diagonal_2"])]:
                    if row+len(current_words["diagonal_2"]) <len(input) and column-len(current_words["diagonal_2"]) >=0:
                        current_words["diagonal_2"].append(input[row+len(current_words["diagonal_2"]), column-len(current_words["diagonal_2"])])        
            else:                 
                if current_words["diagonal_2"] == word:
                    count +=1   
        column -= 1
        if column >=0:
            current_words = {"right": [input[row, column]], "down": [input[row, column]], "diagonal_1": [input[row, column]],  "diagonal_2": [input[row, column]]}
    row -= 1  
    if row >=0 and column >=0:
        current_words = {"right": [input[row, column]], "down": [input[row, column]], "diagonal_1": [input[row, column]],  "diagonal_2": [input[row, column]]}
print(count)

# part 1 chatgpt:
import numpy as np

# Define the word to search
word = "XMAS"
word_length = len(word)

with open(file_path, 'r') as file:
    grid = [list(line.strip()) for line in file]

grid = np.array(grid)
rows, cols = grid.shape

# Helper function to count occurrences in a specific direction
def count_in_direction(delta_row, delta_col):
    count = 0
    for i in range(rows):
        for j in range(cols):
            # Starting position for the word
            r, c = i, j
            match = True
            for k in range(word_length):
                if not (0 <= r < rows and 0 <= c < cols) or grid[r, c] != word[k]:
                    match = False
                    break
                r += delta_row
                c += delta_col
            if match:
                count += 1
    return count

# Count all occurrences in all directions
total_count = 0
directions = [
    (0, 1),  # Right
    (1, 0),  # Down
    (1, 1),  # Diagonal down-right
    (1, -1), # Diagonal down-left
    (0, -1), # Left
    (-1, 0), # Up
    (-1, -1),# Diagonal up-left
    (-1, 1)  # Diagonal up-right
]

for dr, dc in directions:
    total_count += count_in_direction(dr, dc)

print(f"Total occurrences of '{word}': {total_count}")

# part 2
# find A, check if there is MAS in X form around it 
count = 0
for row in range(1, rows-1):
        for column in range(1, cols-1):
            if grid[row, column] == "A":
            # top left forward, bottom left forward
                if (grid[row - 1, column - 1] == "M" and grid[row - 1, column + 1] == "S" and
                        grid[row + 1, column - 1] == "M" and grid[row + 1, column + 1] == "S"):
                        count += 1
            # top left forward, bottom left backward
                if (grid[row - 1, column - 1] == "M" and grid[row - 1, column + 1] == "M" and
                        grid[row + 1, column - 1] == "S" and grid[row + 1, column + 1] == "S"):
                        count += 1
            # top left backward, bottom left forward
                if (grid[row - 1, column - 1] == "S" and grid[row - 1, column + 1] == "S" and
                        grid[row + 1, column - 1] == "M" and grid[row + 1, column + 1] == "M"):
                        count += 1
            # top left backward, bottom left backward
                if (grid[row - 1, column - 1] == "S" and grid[row - 1, column + 1] == "M" and
                        grid[row + 1, column - 1] == "S" and grid[row + 1, column + 1] == "M"):
                        count += 1
print(count)                        
