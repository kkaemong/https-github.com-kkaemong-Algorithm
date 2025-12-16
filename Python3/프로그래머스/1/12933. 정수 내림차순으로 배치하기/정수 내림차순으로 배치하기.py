def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    s = "".join(answer)
    return int(s)