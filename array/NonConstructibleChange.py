def nonConstructibleChange(coins):
    """
    coins = [5,7,2,1,1,3,22]
    output = 20
    """
    coins.sort()
    change = 0

    for coin in coins:
        
        if coin > change+1:
            return change+1

        change += coin
        
    return change+1