list_ = [1,2,3,4,5,6]

def binary_search_error(list_, item):
    # assume list already sorted
    # error:  binary_search(list_, -1), eventually high < low (-2 forever as low=0, (-1+0)//2 - 1 = -2)
    low = 0
    high = len(list_) - 1

    while low != high:
        print(high)
        mid = (low + high) // 2
        if list_[mid] == item:
            return mid
        elif list_[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    if low == high and list_[low] == item:
        return low
    elif low > high:
        return None

def binary_search(list_, item):
    # assume list already sorted
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = (low + high) // 2
        if list_[mid] == item:
            return mid
        elif list_[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None