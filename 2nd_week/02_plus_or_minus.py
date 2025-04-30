numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    answer_count = []
    def calculate_plus_minus(array, target, result, index):
        if len(array) == index:
            if result == target:
                answer_count.append(result)
            return
        calculate_plus_minus(array, target, result + array[index], index + 1)
        calculate_plus_minus(array, target, result - array[index], index + 1)
    calculate_plus_minus(array, target, 0, 0)
    return len(answer_count)

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!