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


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i < j:

            while i < len(s) and not s[i].isalnum() :
                i += 1

            while j >= 0 and not s[j].isalnum():
                j -= 1

            if i <= j :
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False

        return True

            



