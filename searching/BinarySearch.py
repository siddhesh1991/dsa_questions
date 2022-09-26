def binarySearchFlag(array,target):

    length = len(array)
    midIdx = length//2
    left = array[:midIdx]
    right = array[midIdx:]
    middle = array[midIdx]

    if len(left) > 0 and len(right) > 0:
        if target < middle:
            return binarySearchFlag(left,target)
        elif target > middle:
            return binarySearchFlag(right,target)
        else:
            return True
    else:
        return False


def binarySearchIdx(array,left,right,target):

    middle = (left+right)//2
    if left <= right:

        if target < array[middle]:
            return binarySearchIdx(array,left,middle-1,target)
        elif target > array[middle]:
            return binarySearchIdx(array,middle+1,right,target)
        else:
            return middle

    else:
        return -1

def binarySearchIdxItr(array,target):

    left = 0
    right = len(array)-1

    while left <= right:
        middle = (left+right)//2

        if target < array[middle]:
            right = middle -1
        elif target > array[middle]:
            left = middle + 1
        else:
            return middle

    return -1