def solution(my_string, num1, num2):
    answer = list(my_string)
    ans = ''
    for i in range(len(answer)):
        if i == num1:
            answer[num1], answer[num2] = answer[num2],answer[num1]
        ans += answer[i]
    return ans