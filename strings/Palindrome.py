def isPalindrome(string):
    # Write your code here.
    if len(string) == 1:
        return True
        
    left = 0 
    right = len(string)-1
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False

    return True

def isPalindrome(string):
    stringArr = list(string)
    stringArrReverse = stringArr[::-1]
    return stringArr == stringArrReverse
