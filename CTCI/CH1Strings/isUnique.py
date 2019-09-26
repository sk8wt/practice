#sk8wt
#9/13/2018
#problem 1.1

'''
Runtime of this algorithm is O(n), where each value in the string needs to be checked
Space complexity of this algorithm is O(1) since a constant amount of space is allocated
'''
def isUnique(sentence):
    sentence_list = [None] * 128

    for i in range(0, len(sentence)):
        index_value = ord(sentence[i])
        if sentence_list[index_value] != None:  
            return False
        sentence_list[index_value] = 1
    return True

print(isUnique("poiuytrewqlkjhgfdsamnbvcxz"))