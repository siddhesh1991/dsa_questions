def sortedSquaredArray(array):
    """
    array = [-5,-4,0,1,2]
    output = [0,1,4,16,25]
    """
    sortedSquareArr = [0 for _ in len(array)]
    smallIdx = 0
    largeIdx = len(array)-1

    for idx in reversed(range(len(array))):
        smallValue = array[smallIdx]
        largeValue = array[largeIdx]

        if abs(smallValue) > abs(largeValue):

            sortedSquareArr[idx] = smallValue**2
            smallIdx += 1
        else:
            sortedSquareArr[idx] = largeValue*2
            largeIdx -= 1

    return sortedSquareArr
