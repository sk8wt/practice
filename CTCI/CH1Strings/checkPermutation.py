#sk8wt
#9/13/2018
#Given 2 strings, write a method to decide if one is a permutation of the other

'''
Runtime: O(3N) --> O(N), since each for loop reads in a string of size N
Space allocation: O(3N)?
'''
def check_permutation(string1, string2):

    letter_dict = {}

    #check to see if strings are equal
    if (len(string1) != len(string2)):
        return False

    #store first string letters into a dictionary
    for i in string1:
        letter = i
        if (letter in letter_dict):
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    #check to see if second string's letters match
    for j in string2:
        second_letter = j
        if (second_letter in letter_dict):
            letter_dict[second_letter] -= 1
        else:
            return False

    #verify that strings are equal
    for k in letter_dict:
        if letter_dict[k] != 0:
            return False
    return True

print(check_permutation("asdf", "asdff"))
print(check_permutation("asdf", "asdf"))
