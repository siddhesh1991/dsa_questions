def firstNonRepeatingCharacter(string):
    # Write your code here.
    hashMap = {}
    for char in string:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1

    for idx in range(len(string)):
        if hashMap[string[idx]] == 1:
            return idx

    return -1
        