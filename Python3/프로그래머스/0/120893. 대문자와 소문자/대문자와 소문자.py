def solution(my_string):
    answer = ""
    for ch in my_string:
        if ch.islower():       # 소문자면 대문자로
            answer += ch.upper()
        else:                  # 대문자면 소문자로
            answer += ch.lower()
    return answer