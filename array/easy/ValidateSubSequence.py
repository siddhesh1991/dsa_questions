def isValidSubsequence(array, sequence):
    # Write your code here.
    """
    array = [5,1,22,25,6,-1,8,10]
    sequence = [1,6,-1,10]
    o/p: True
    """
    seqIndex = 0
    for i in array:
        if seqIndex >= len(sequence):
            break
            
        if i == sequence[seqIndex]:
            seqIndex += 1
            
    return seqIndex == len(sequence)