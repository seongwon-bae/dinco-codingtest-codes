input = input()

# num은 0 또는 1
# numm이 0 이면 1->0로 바꿀 때의 횟수, 1이면 0->1로 바꿀 때의 횟수
def number_reverse(string, num):
    count = 0
    first_index = -1
    for index in range(len(string)):
        if first_index > -1:
            if string[index] == str(num):
                count += 1
                first_index = -1
            else:
                continue
        else:
            if string[index] == str(num):
                continue
            else:
                first_index = index
    return count

def find_count_to_turn_out_to_all_zero_or_all_one(string):

    # 1->0으로 바꾸기
    zero_to_one = number_reverse(string, 1)

    # 0->1로 바꾸기
    one_to_zero = number_reverse(string, 0)

    if zero_to_one>one_to_zero:
        return zero_to_one
    else:
        return one_to_zero


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)