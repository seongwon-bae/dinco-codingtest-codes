def find_max_plus_or_multiply(array):
    previous = ''
    max = 0
    for element in array:
        if max * element > max+element:
            max *= element
        else:
            max += element
        # if element <= 1 or max <= 1:
        #     max += element
        # else:
        #     max *= element
    return max


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))