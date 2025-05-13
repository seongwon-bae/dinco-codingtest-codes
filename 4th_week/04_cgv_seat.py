seat_count = 9
vip_seat_array = [4, 7]


def find_all_case(number_count):
    numbers = [x for x in range(number_count)]

memo = {
    1: 1,
    2: 2
}
def fibo_dp(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    fibo_memo[n] = fibo_dp(n-1, fibo_memo) + fibo_dp(n-2, fibo_memo)
    return fibo_memo[n]

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_way = 1
    for seat in range(len(fixed_seat_array)+1):
        if seat == 0:
            all_way *= fibo_dp(fixed_seat_array[seat]-1,memo)
        elif seat == len(fixed_seat_array):
            all_way *= fibo_dp(total_count-fixed_seat_array[seat-1], memo)
        else:
            all_way *= fibo_dp(fixed_seat_array[seat]-fixed_seat_array[seat-1]-1, memo)
    return all_way


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))