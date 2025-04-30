input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        is_prime = True
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                is_prime = False
                break
        if is_prime:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)