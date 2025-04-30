def summarize_string(input_str):
    previous_string = ''
    answer_string = ''
    same_count=0
    for i in range(len(input_str)):
        if i==0:
            previous_string = input_str[i]
            same_count += 1
            continue
        if previous_string == input_str[i]:
            same_count += 1
        else:
            answer_string += f'{previous_string}{same_count}/'
            same_count = 1
            previous_string = input_str[i]
    else:
        answer_string += f'{previous_string}{same_count}'
    return answer_string
input_str = "acccdeee"

print(summarize_string(input_str))