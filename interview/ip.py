import csv

source_dict = {}
dest_dict = {}

with open('queries.txt', 'rb') as csvfile:
    queries = csv.reader(csvfile, delimiter=',')
    print(queries)
    for row in queries:
        if (len(row) < 4):
            continue
        if (row[0] in source_dict):
            source_dict[row[0]] += 1
        else: 
            source_dict[row[0]] = 1
        if (row[1] in dest_dict):
            dest_dict[row[1]] += 1
        else: 
            dest_dict[row[1]] = 1
#print(csvfile)

print("Source: ", source_dict)
print("Dest: ", dest_dict)

## inefficient version
## TODO: improve later
def findN(dict_list, n):
    max_key = 0
    count = 0
    max_val = 0
    final_list = []

    while (count < n):
        for key in dict_list:
            value = dict_list[key]
            if (value > max_val):
                max_val = value
                max_key = key
        ## removing largest value from dictionary
        dict_list.pop(max_key, None)   
        count += 1
        final_list.append([max_key, max_val])
        max_key, max_val = 0, 0

    return final_list

print("---------")
dest = findN(dest_dict, 4)
print(dest)

source = findN(source_dict, 4)
print(source)