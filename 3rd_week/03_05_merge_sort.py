array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    index1, index2 = 0,0
    result = []
    while index1<len(array1) or index2<len(array2):
        if index1==len(array1):
            result.append(array2[index2])
            index2 += 1
            # print('result',result)
            continue
        elif index2==len(array2):
            result.append(array1[index1])
            index1 += 1
            continue
        if array1[index1] < array2[index2]:
            result.append(array1[index1])
            index1 += 1
        else:
            result.append(array2[index2])
            index2 += 1
    return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid])   # 왼쪽 부분을 정렬하고
    right_array = merge_sort(array[mid:])  # 오른쪽 부분을 정렬한 다음에
    merge(left_array, right_array)         # 합치면서 정렬하면 됩니다!