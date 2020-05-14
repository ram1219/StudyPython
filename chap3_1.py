# bool 자료형과 if 조건문 학습

x = 10
under_20 = x < 20
print("under_20 : ", under_20)
print("not under_20 : ", not under_20)          # not 연산자  x >= 20

print(True and False)                           # and 연산자
print(True or False)                            # or 연산자

# 날짜/시간과 관련된 기능 import
import datetime

# if 연산자
now = datetime.datetime.now()                  # 현재 날짜/시간 

print(now.year, "년", now.month, "월", now.day, "일")
print(now.hour, "시", now.minute, "분", now.second, "초")

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# 오전 오후 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

# 계절 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))
elif 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다.".format(now.month))
elif 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))
else
    print("이번 달은 {}월로 겨울입니다.".format(now.month))

# in 연산자 활용
number = input("정수 입력 > ")
last_character = number[-1]                        # 입력받은 문자열의 마지막 값을 가져온다.

if last_character in "02468":
    print("짝수입니다.")
else:
    print("홀수입니다.")

    
# pass 키워드
number = int(number)

if number > 0:
    pass                                            # 미구현 상태. 임시적으로 비워둠
else:
    pass