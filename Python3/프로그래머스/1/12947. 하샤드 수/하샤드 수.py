def solution(x):
    t = sum(list(map(int, list(str(x)))))
    if x % t == 0:
        return True
    else:
        return False
print(solution(11))
