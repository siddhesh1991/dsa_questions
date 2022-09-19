def runLengthEncoding(string):
    # Write your code here.
    curChar = string[0]
    cipher = []
    counter = 0 
    
    for idx in range(1,len(string)):
        print(string[idx])
        if string[idx] == curChar:                
            counter += 1
        else:
            counter += 1
            cipher.append(str(counter)+curChar)
            counter = 0
            
        if counter >= 9:
            cipher.append(str(counter)+curChar)
            counter = 0
        
        curChar = string[idx]

    counter += 1
    cipher.append(str(counter)+curChar)
    cipher = "".join(cipher)
    
    return cipher