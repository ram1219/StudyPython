# 리스트와 반복문 학습

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