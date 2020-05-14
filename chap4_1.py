# 리스트 학습

# 리스트의 연결 , 반복, 길이
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("list_a + list_b = ", list_a + list_b)
print("list_a * 3 = ", list_a * 3)
print("len(list_a) = ", len(list_a))
print()

# 리스트에 요소 추가
list_a.append(4)                    # 리스트의 뒤에 요소 추가
list_a.insert(2, 10)                # 앞의 자리에 뒤에 숫자 추가
print(list_a)

list_a.extend([5, 6, 7])            # 리스트의 뒤에 새로운 요소 전체 추가
print(list_a)

# 리스트에 요소 제거
del list_a[2]                       # 리스트의 요소 하나 제거하기
print("del list_a[2] : ", list_a)

list_a.pop(1)
print("pop(1) : ", list_a)

del list_b[:2]                      # del 키워드는 지정한 범위만큼 제거 가능

list_a.remove(7)                    # 값으로 지정해서 제거
print(list_a)

list_b.clear()                      # 전체 리스트 내부 요소 제거
print(list_b)

# in / not in 연산자
list_a = [273, 32, 103, 57, 52]
print(273 in list_a)                # 273이 list_a 안에 있을 경우 True 출력
print(273 not in list_a)            # 273이 list_a 안에 있을 경우 False 출력