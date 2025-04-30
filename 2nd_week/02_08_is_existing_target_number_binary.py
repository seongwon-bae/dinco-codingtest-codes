finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    count = 0
    start = 0
    last = len(array)-1
    now = (start+last)//2
    while 1:
        count+=1
        if array[now] > target:
            last = now-1
        elif array[now] < target:
            start = now+1
        else:
            print(count)
            return True
        now = (start+last)//2
    return Flase


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)