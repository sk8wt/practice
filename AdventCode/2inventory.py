# sk8wt
# 1/5/19
# Day 2: Inventory Management System

'''
Problem Statement:
- Given an array with a string of letters, check how many times each letter appears
- If it's 2 times, add to the 2 count. If it's 3 times, add to the 3 count. If a combination of both, add to both counts
- If one specific count shows up multiple times, that only counts once
- Return three_count * two_count
    abcde: doesn't count for either
    aaabbb: counts for the 3 (1 time)
    aabbb: counts for the 2(1 time) and the 3 (1 time)
    bbbbbb: counts for the 3 (1 time)

Pseudocode:
1) Read in the document as an array of strings
2) Call the hash_letters(array[i]) function

    hash_letters(ID):
        letter_dictionary = {}
        two_count = 0
        three_count = 0
        for letter in ID:
            if letter in letter_dictionary:
                letter_dictionary[letter] += 1
            else:
                letter_dictionary[letter] = 0

        for letter_key in letter_dictionary:
            if letter_dictionary[letter_key] == 2 and two_count < 1:
                two_count = 1
            if letter_dictionary[letter_key] >= 3 and three_count < 1:
                three_count = 1
        return two_count, three_count

3) Look through the remaining ID numbers, add function return value to two_count and three_count values
4) Multiply the variables together, return as final answer
'''

def hash_letters(ID):
    letter_dictionary = {}
    num_twos = 0
    num_threes = 0

    for letter in ID:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1

    for letter_key in letter_dictionary:
        if letter_dictionary[letter_key] == 2 and num_twos < 1:
            num_twos = 1
        if letter_dictionary[letter_key] >= 3 and num_threes < 1:
            num_threes = 1
    return num_twos, num_threes


total = []
file = open("inventory.txt")
for lines in file:
    lines = lines.strip()
    total += (lines.split('\t'))

two_count = 0
three_count = 0

for word in total:
    local_two, local_three = hash_letters(word)
    two_count += local_two
    three_count += local_three

final = two_count * three_count
print(final)