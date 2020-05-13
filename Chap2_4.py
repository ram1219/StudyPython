# 숫자와 문자열을 다양한 형태로 출력
format_b="{} 열공하여 첫 연봉 {}만원 만들기".format("파이썬",3000)
print(format_b)

# 문자열 전체 공백제거 - strip(), 왼쪽 공백 제거 - lstrip(), 오른쪽 공백 제거 - rstrip() 
strip_a = """
    안녕하세요
제 이름은 김가람입니다.
"""
print(strip_a.strip())

# 문자열 대,소문자 변환
upper_a = "abcde"
print(upper_a.upper())

lower_a = "HelLo WorlD"
print(lower_a.lower())

# 문자열 찾기 및 확인
find_a = "안녕하세요".find("녕")
print(find_a)

print("안녕" in "안녕하세요")

# 문자열을 특정한 문자로 자름 -> 결과는 리스트로 출력
a = "10,20,30,40,50".split(",")
print(a)