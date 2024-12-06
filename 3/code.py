import re 

# part 1
multiplications = []
with open('/Users/ummi/Documents/Traineeship/advent_of_code/3/input.txt', 'r') as file:
    for line in file:
        all_mult = re.findall("mul\(\d+,\d+\)",line)
        multiplications = multiplications + all_mult

sum = 0
for multiplication in multiplications:
    value_1 = int(multiplication.split(",")[0].split("(")[1])
    value_2 = int(multiplication.split(",")[1].split(")")[0])
    sum += value_1*value_2
print(sum)    

# part 2
multiplications = []
with open('/Users/ummi/Documents/Traineeship/advent_of_code/3/input2.txt', 'r') as file:
    for line in file:
        all_mult = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)",line)
        multiplications = multiplications + all_mult

sum = 0
do = True
for multiplication in multiplications:
    if multiplication == "do()":
        do = True
    elif multiplication == "don't()":
        do = False
    if do and multiplication != "do()" and multiplication != "don't()":        
        value_1 = int(multiplication.split(",")[0].split("(")[1])
        value_2 = int(multiplication.split(",")[1].split(")")[0])
        sum += value_1*value_2
print(sum) 