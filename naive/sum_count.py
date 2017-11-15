def sum_recursive(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_recursive(numbers[1:])

def count_recursive(list_):
    if len(list_) == 0:
        return 0
    else:
        return 1 + count_recursive(list_[1:])

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

a = [1,2,3,4,5]
b = []

print('a:')
print('sum_r: {}, sum_l: {}'.format(sum_recursive(a), sum_loop(a)))
print('count_r: {}, count_l: {}'.format(count_recursive(a), count_loop(a)))

print('b:')
print('sum_r: {}, sum_l: {}'.format(sum_recursive(b), sum_loop(b)))
print('count_r: {}, count_l: {}'.format(count_recursive(b), count_loop(b)))
