#Vi ska snacka om Ordo idag. 
#Tids komplexitet på algoritmer
#Binär sökning
# O upphöjd till 2. 

#bubble sort
# selection sort
#Insert sort
#Shell sort


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid + 1
        else:
            return mid
    return - 1
arr = [2,3,4,10,40]
x = 40

result = binary_search(arr,x)
#if result is not 1:
#   print (element )