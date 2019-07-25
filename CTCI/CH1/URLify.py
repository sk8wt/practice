# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.


def URLify(sentence):
    new_sentence = ""
    for character in sentence:
        if (character == " "):
            character = "%20"
            new_sentence += character
        new_sentence += character
    return new_sentence


print(URLify("hello"))
print(URLify("hello my name is"))
print(URLify("hello my  name   is"))
print(URLify(" hello my  name   is"))
print(URLify("hello my  name   is "))
print(URLify(""))
