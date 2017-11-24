import random

list_ = [4,1,2,6,3,5]

def quick_sort(list_):
    if len(list_) < 2:
        return list_
    else:
        pivot = list_[0]
        child_list_left = []
        child_list_right = []

        for e in list_[1:]:
            if e <= pivot:
                child_list_left.append(e)
            else:
                child_list_right.append(e)
        return quick_sort(child_list_left) + [pivot] + quick_sort(child_list_right)

def quick_sort_r(list_):
    # random choose pivot
    if len(list_) < 2:
        return list_
    else:
        pivot_i = random.choice(range(len(list_)))
        pivot = list_[pivot_i]
        child_list_left = []
        child_list_right = []

        for e in list_[:pivot_i] + list_[pivot_i+1:]:
            if e <= pivot:
                child_list_left.append(e)
            else:
                child_list_right.append(e)
        return quick_sort(child_list_left) + [pivot] + quick_sort(child_list_right)


print('origianl list: {}, sorted list: {}'.format(list_, quick_sort(list_)))
print('origianl list: {}, sorted list: {}'.format(list_, quick_sort_r(list_)))