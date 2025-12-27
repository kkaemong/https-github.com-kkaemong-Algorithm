def solution(numbers):
    a = set(range(10))
    b = set(numbers)
    return sum(a - b)