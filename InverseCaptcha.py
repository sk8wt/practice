#sk8wt
#9/13/18

'''
GOAL: Given a list, output the totatl sum of adjacent numbers

- Read in the list
- Create a double for loop
    - If previous == next, store that integer. If more are the same, add that int
    - If first == last, add that number to sum
- Return sum

'''
def find_sum(list):

    sum = 0

    for i in range(0, len(list)-1):
        if (list[i] == list[i+1]):
            sum += int(list[i])

    if (list[0] == list[-1]):
        sum += int(list[0])
    return sum


value = input("What values would you like to insert? ")

answer = find_sum(value)
print(answer)