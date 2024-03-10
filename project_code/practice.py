football = {
    "Spain" : 4,
    "France" : 3,
    "Germany" : 7
}

def dictToList(dictionary):
    football = []
    keys = dictionary.keys()

    for key in keys:
        football.append([key, dictionary[key]])
    return football

def merge(merged, list_1, list_2, key):
    index_1 = 0
    index_2 = 0
    index_merged = 0
    while index_1 < len(list_1) and index_2 < len(list_2):
        if key(list_1[index_1]) < key(list_2[index_2]):  # comparision line
            merged[index_merged] = list_1[index_1]
            index_1 = index_1 + 1
        else:
            merged[index_merged] = list_2[index_2]
            index_2 = index_2 + 1
        index_merged = index_merged + 1

    while index_1 < len(list_1):
        merged[index_merged] = list_1[index_1]
        index_1 = index_1 + 1
        index_merged = index_merged + 1

    while index_2 < len(list_2):
        merged[index_merged] = list_2[index_2]
        index_2 = index_2 + 1
        index_merged = index_merged + 1
    return merged

def merge_sort(items, key):
    if len(items) < 2:
        return items
    else:
        midpoint = len(items) // 2
        left_half = items[:midpoint]
        right_half = items[midpoint:]

    left_half = merge_sort(left_half, key)
    right_half = merge_sort(right_half, key)
    result = merge(items, left_half, right_half, key)
    return result

def keyCountry(country):
    return country[0]

def keyGoalScored(country):
    return country[1]

footballList = dictToList(football)
print(footballList)
merge_sort(footballList, keyGoalScored)
print(footballList)