from collections import deque

balanced_parentheses_string = "()))((()"

def is_balanced(string):
    balance_count = 0
    for char in string:
        if char == '(': balance_count += 1
        elif char == ')': balance_count -= 1
    if balance_count == 0: return True
    else: return False

def is_correct(string):
    parentheses_stack = []
    result = True
    for char in string:
        if char == '(':
            parentheses_stack.append(char)
        elif char == ')':
            if len(parentheses_stack) == 0:
                result = False
                break
            elif parentheses_stack[-1] == '(':
                parentheses_stack.pop()
            else:
                result = False
    if len(parentheses_stack) > 0:
        result = False
    return result

def split_string(string):
    split_index = 1
    u = ''
    v = ''
    while split_index <= len(string):
        u = string[0:split_index]
        v = string[split_index:]
        if is_balanced(u): break
        split_index+=1
    return u,v

def reverse_parentheses_string(string):
    result = ''
    for char in string:
        if char == '(': result += ')'
        elif char == ')': result += '('
    return result

def get_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == '':
        return ''
    u,v = split_string(balanced_parentheses_string)
    if is_correct(u):
        return u + get_correct_parentheses(v)
    else:
        return '('+get_correct_parentheses(v)+')'+reverse_parentheses_string(u[1:-1])


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))