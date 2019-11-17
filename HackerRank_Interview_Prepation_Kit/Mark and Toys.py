def maximumToys(prices, k):
    prices.sort()
    sum = 0
    count_toys = 0
    for i in prices:
        if sum+i < k:
            sum = sum +i
            count_toys = count_toys +1
    return count_toys