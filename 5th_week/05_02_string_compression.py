input = "abcabcabcabcdededededede"


# 1. 문자열을 1개씩, 2개씩, 3개씩 ... 2/n개까지 나눈다.
# 2. 나눈 문자열들을 차례대로 돌면서 현재 인덱스와 다음 인덱스가 동일한지 비교한다.
# 3. 인덱스가 동일하다면 카운트를 증가, 동일하지 않다면 최종 문자열 리스트에 추가한다.
# 4. 최종 문자열 리스트에 추가 시 카운트가 1이라면 1을 붙일 필요가 없다.
def string_compression(string):
    n = len(string)
    string_lengths = []
    for i in range(int(n/2)):
        splited_string = [string[x:x+i+1] for x in range(0,n,i+1)]
        count = 1
        result_string = ''
        for j in range(len(splited_string)-1):
            if splited_string[j] == splited_string[j+1]:
                count += 1
            else:
                if count != 1:
                    result_string += f'{count}{splited_string[j]}'
                    count = 1
                else:
                    result_string += f'{splited_string[j]}'
        if count==1:
            result_string += f'{splited_string[j+1]}'
        else:
            result_string += f'{count}{splited_string[j]}'
        string_lengths.append(len(result_string))
    if len(string) == 1:
        string_lengths.append(1)
    return min(string_lengths)


print(string_compression(input))  # 14 가 출력되어야 합니다!
print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))