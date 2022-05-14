import random as rand

width = 10
height = 20

matrix = []
rows_with_5 = []
for i in range(height):
    temporary_list_of_vars = []
    five_count = 0
    is_current_row_include_fives = False
    for j in range(width):
        rand_value = rand.randint(0, 15)
        if(rand_value == 5):
            five_count += 1
        if(five_count >= 3 and is_current_row_include_fives == False):
            rows_with_5.append(i)
            is_current_row_include_fives = True
        temporary_list_of_vars.append(rand_value)
    matrix.append(temporary_list_of_vars)

for i in matrix:
    print(i)

print("\n", rows_with_5)