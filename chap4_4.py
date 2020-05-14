# 문자열, 리스트, 딕셔너리와 관련된 기본 함수 학습

# 리스트에 적용할 수 있는 기본 함수
numbers = [103, 52, 273, 32, 77]
print(min(numbers))                         # 리스트 내부의 최소값
print(max(numbers))                         # 리스트 내부의 최대값
print(sum(numbers))                         # 리스트 내부의 모든 요소들의 합
print()

for i in reversed(numbers):                 # 리스트 내부 요소를 역방향으로 출력
    print(i)
print()

print(list(enumerate(numbers)))             # 리스트 내부 요소의 값과 위치 확인 
print()


# 딕셔너리의 items() 함수 사용
example_dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C",
}

print("ittems() 함수 사용 : ", example_dictionary.items())  # 딕셔너리에 있는 키와 값을 출력