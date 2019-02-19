import sys
sys.stdin = open("계산기3.txt")

for tc in range(10):
    N = int(input())
    input_string = input()
    string_stack = []
    operator_stack = []
    operator = {"(": 0,
                "+": 1,
                "*": 2}
    parentheses = "()"
    result = []

    for i in input_string:
        if i not in operator and i not in parentheses:
            string_stack.append(i)
        elif i == "(":
            operator_stack.append(i)
        elif i == ")":
            while operator_stack[-1] != "(":
                if operator_stack[-1] == "+":
                    operator_stack.pop()
                    string_stack.append(int(string_stack.pop()) + int(string_stack.pop()))
                elif operator_stack[-1] == "*":
                    operator_stack.pop()
                    string_stack.append(int(string_stack.pop()) * int(string_stack.pop()))
            operator_stack.pop()
        else:
            if len(operator_stack) >= 1:
                if operator[i] > operator[operator_stack[-1]]:
                    operator_stack.append(i)
                else:
                    while operator_stack and operator[operator_stack[-1]] >= operator[i]:
                        if operator_stack[-1] == "+":
                            operator_stack.pop()
                            string_stack.append(int(string_stack.pop()) + int(string_stack.pop()))
                        elif operator_stack[-1] == "*":
                            operator_stack.pop()
                            string_stack.append(int(string_stack.pop()) * int(string_stack.pop()))
                    operator_stack.append(i)
            else:
                operator_stack.append(i)

    for i in range(len(operator_stack)):
        if operator_stack[-1] == "+":
            operator_stack.pop()
            string_stack.append(int(string_stack.pop()) + int(string_stack.pop()))
        elif operator_stack[-1] == "*":
            operator_stack.pop()
            string_stack.append(int(string_stack.pop()) * int(string_stack.pop()))

    print(f'#{tc+1} {string_stack[0]}')

