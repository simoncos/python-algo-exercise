def sum_recursive(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        # method 1
        return numbers.pop() + sum_recursive(numbers)
        # method 2: better not edit original data
        # return numbers[0] + sum_recursive(numbers[1:])

def sum_loop(numbers):
    result = 0
    for n in numbers:
        result += n
    return result

def count_loop(list_):
    result = 0
    while len(list_) != 0:
        result += 1
        list_.pop()
    return result

def count_recursive(list_):
    if len(list_) == 0:
        return 0
    else:
        # method 1
        list_.pop()
        return 1 + count_recursive(list_)
        # method 2: better not edit original data
        # return 1 + list_[:1]