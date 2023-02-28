import math
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find = 8
low = 0
high = len(list)
mid = high//2

while mid < high or mid > low:
    if list[mid] > find:
        high = mid - 1
        mid = (low + high)//2
    elif list[mid] < find:
        low = mid + 1
        mid = (low + high)//2
    elif list[mid] == find:
        return mid