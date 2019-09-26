def compression(sentence):
    letter_counter = 0
    last_letter = sentence[0]
    new_sentence = ""

    for character in sentence:
        if character == last_letter:
            letter_counter += 1
        else:
            new_sentence += last_letter
            new_sentence += str(letter_counter)
            letter_counter = 1
        last_letter = character

    return (new_sentence, sentence)[len(new_sentence) > len(sentence)]


print(compression("ab"))
print(compression("abcd"))
print(compression("aabcdddaaaaa"))
print(compression("abcdefghi"))
