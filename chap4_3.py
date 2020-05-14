# 범위, 반복 함수 학습

# 범위 range
print(list(range(10)))                      # 0부터 n-1 까지
print(list(range(1,11)))                    # n부터 m-1 까지
print(list(range(1,11,2)))                  # n부터 m-1 까지, p만큼의 차이

# 변수를 사용한 range
n = 10
print(list(range(1, 10//2)))                # // --> 나누기 연산한 몫을 정수형으로 나타냄. (/를 사용할 경우 에러발생)

# for문
array = [11, 22, 33, 44, 55, 66, 77]
for i in range(len(array)):                 # array의 길이만큼 반복
    print(i, "번째 array : ", array[i])

# while문
i = 0
while i < 3:
    print("{}번째 반복입니다.".format(i))
    i += 1

list_test = [1, 2, 1, 2]
value_l = 2

while value_l in list_test:                 # value_l 의 값이 list_test에 존재하는 동안 반복
    list_test.remove(value_l)               # value_l 의 값이 list_test에 있으면 제거

print(list_test)

# 시간 관련된 기능 import
import time

number = 0

target_tick = time.time() + 5               # time.time()은 유닉스 타임 
while time.time() < target_tick:            # 5초 동안 반복
    number += 1

print("5초 동안 {}번 반복했습니다.".format(number))


