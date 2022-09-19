def getLetter(char,key):
    ascii = ord(char)+key
    if ascii > 122:
        ascii = (96+(ascii - ord("z"))%26)

    letter = chr(ascii)
    return letter
    
def caesarCipherEncryptor(string, key):
    """
    string = "xyz"
    key = 2
    op = "zab"
    """
    return "".join([getLetter(i,key) for i in string])
