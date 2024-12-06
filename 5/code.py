# part 1 

file_path = '/Users/ummi/Documents/Traineeship/advent_of_code/5/input.txt'

rules = {}
updates = []
updates_list = []
with open(file_path, 'r') as file:
    data = file.read().strip().split('\n\n') 
    rules_input = data[0].split('\n')
    for rule in rules_input:
        left, right = rule.split('|')
        if int(left) in rules.keys():
            rules[int(left)].append(int(right))
        else:    
            rules[int(left)] = [int(right)]
    updates_input = data[1].split('\n')
    for update_str in updates_input:
        update_dict = {}
        update_list = []
        update = update_str.split(",")
        for i in range(len(update)):
            update_dict[int(update[i])] = i
            update_list.append(int(update[i]))
        updates.append(update_dict)    
        updates_list.append(update_list)

count = 0
for i in range(len(updates)):
    update = updates[i]
    nice = True
    for left,rights in rules.items():
        for right in rights:
            if left in update.keys() and right in update.keys():
                if update[left] > update[right]:
                    nice = False
                    break     
    if nice:
        middle = len(update.keys()) // 2
        count += updates_list[i][middle]

print(count)

# part 2

all_rules = sum(len(value) for value in rules.values())
count = 0

for i in range(len(updates)):
    update = updates[i]
    correct_please = False
    
    # Keep reordering until all rules are satisfied
    while True:
        nice = 0  # Reset the count of satisfied rules
        for left, rights in rules.items():
            for right in rights:
                if left in update.keys() and right in update.keys():
                    # If rule is violated, swap the positions of left and right
                    if update[left] > update[right]:
                        correct_please = True
                        tmp = update[left]
                        update[left] = update[right]
                        update[right] = tmp   
                    else:
                        nice += 1  # Rule is satisfied
                else:
                    nice += 1  # Rule doesn't apply because one of the pages is missing
        
        # If all rules are satisfied, break out of the loop
        if nice == all_rules:
            break

    # If corrections were made, calculate the middle page of the corrected update
    if correct_please:
        middle = len(update.keys()) // 2
        updated_list = []
        for value, place in sorted(update.items(), key=lambda x: x[1]):
            updated_list.append(value)  # Recreate the sorted list
        count += updated_list[middle]

print(count)

