# 재귀함수 학습

# 팩토리얼 함수 선언
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 재귀함수의 속도를 빠르게 하기 위한 메모화 --> 같은 값을 한 번만 연산
dictionary = {
    1: 1,
    2: 2
}

# 피보나치 수열 함수 선언
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]                                # 메모가 되어 있으면 메모된 값을 리턴
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)        # 메모가 되어 있지 않은 경우 연산
        dictionary[n] = output
        return output

# 메인
print("5! = ", factorial(5))
print()

print("fibonacci(3) : ", fibonacci(3))