PI = 3.14159265

# print("모듈")
# print(__name__)

# 숫자 입력받는 함수 생성
def number_input():
    output = input("숫자 입력 : ")   
    return float(output)                        # 입력받은 문자열을 float 현식으로 변홧시켜 리턴

# 원의 둘레 구하는 함수 생성
def get_circumference(radius):
    return 2 * PI * radius

# 원의 넓이 구하는 함수 생성
def get_circle_area(radius):
    return PI * radius * radius

if __name__ == "__main__":                  # 실행하는 파일의 __name__ 이 __main__ 인 경우만 아래 실행
    print("get_circumference(10)", get_circumference(10))
    print("get_circle_area(10)", get_circle_area(10))