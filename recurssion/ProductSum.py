def productSum(array,level=1):
    """
    The product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 + (y + z); the product sum of
    [x, [y, [z]]] is x + 2 + (y + 3z).
    
    Sample Input
    array [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

    Sample Output
    12 // calculated as: 5 + 2 + 2 (7-1) + 3 + 2 (6 + 3 (-13+8) + 4)
    """
    total = 0

    for value in array:
        
        if type(value) is list:
            total += productSum(value,level+1)
        else:
            total += value
            
    return total * level
