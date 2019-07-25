# sk8wt
# 7/23/19

'''
Trying to see if I can improve performance from the way I approached the problem last year
'''


def oneAway(sentence1, sentence2):
    if (abs(len(sentence1) - len(sentence2)) > 1):
        return False

    # order is (false, true)[conditional]
    longer = (sentence2, sentence1)[len(sentence1) > len(sentence2)]
    other_sentence = (sentence1, sentence2)[len(sentence1) > len(sentence2)]

    i = 0
    diff_count = 0
    for character in other_sentence:
        if character != other_sentence[i]:
            diff_count += 1

        if diff_count > 1:
            return False
        i += 1

    if (len(longer) != len(other_sentence) and longer[i] != character):
        if (diff_count > 1):
            return False

    return True


print(oneAway("pale", "ple"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))

print("###########################")

# sk8wt
# 9/15/18
'''
GOAL: Given two strings, check if the strings are one or 0 edits away

Runtime analysis: O(2N) which simplifies into O(N) bc reading in the content of both strings
Space analysis: O(2N) which simplifies into O(N)
'''


def palindrome_permutation(string1, string2):
    letter_dict = {}

    if (abs(len(string1) - len(string2)) >= 2):
        return False

    for letter in string1:
        if (letter in letter_dict):
            letter_dict[letter] += 1

        else:
            letter_dict[letter] = 1

    for second_letter in string2:
        if (second_letter in letter_dict):
            letter_dict[second_letter] -= 1
        else:
            letter_dict[second_letter] = 1
        if (letter_dict[second_letter] >= 2 or letter_dict[second_letter] <= -2):
            return False

    num_diffs = 0

    for diff in letter_dict:
        if (letter_dict[diff] == 1):
            num_diffs += 1
        if (num_diffs > 2):
            return False
    return True


print(palindrome_permutation("pale", "ple"))
print(palindrome_permutation("pales", "pale"))
print(palindrome_permutation("pale", "bale"))
print(palindrome_permutation("pale", "bake"))
