def generateCounter(string):
    hashMap = {}
    for i in string :  
        if i not in hashMap:
            hashMap[i] = 1
        else:
            hashMap[i] += 1
    return hashMap
    
def generateDocument(characters, document):
    charMap = generateCounter(characters)
    docMap = generateCounter(document)

    for i in docMap.keys():
        if i in charMap and charMap[i] >= docMap[i]:
            pass
        else:
            return False
    return True