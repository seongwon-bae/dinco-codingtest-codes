def find_max_occurred_alphabet(string):
    alphabets = [0 for i in range(0,26)]

    # ord('a') -> 97
    for bet in range(len(string)):
        if string[bet].isalpha():
            alphabets[ord(string[bet])-ord('a')] += 1

    max_count = alphabets[0]
    max_index = 0
    for index in range(len(alphabets)):
        if alphabets[index] > max_count:
            max_count = alphabets[index]
            max_index = index
    return chr(ord('a')+max_index)


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

