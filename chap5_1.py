# 함수 학습

# 함수 생성 
def print_n_times(value, n):
    for i in range(n):
        print(value)

# 가변 매개변수
def n_times(n, *values):
    for i in range(n):
        for value in values:                            # values는 리스트처럼 활용
            print(value)
        print()

# 함수의 활용
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

# 키워드 매개변수를 활용한 함수의 활용
def sum_def(start = 0, end = 100, step = 1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output

# 메인
print_n_times("안녕하세요", 3)
print()
n_times(3, "안녕하세요", "즐거운", "파이썬")
print()

print("0 to 100 : ", sum_all(0, 100))
print()

print("0부터 100까지 10 단위의 합 = ", sum_def(0, 100, 10))
print("0부터 50까지 2 단위의 합 = ", sum_def(end = 50, step = 2))