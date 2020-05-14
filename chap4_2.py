# 딕셔너리 -> 여러 개의 값을 나타낼 수 있게 해주는 자료형
# 딕셔너리 선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : [ "망고", "설탕", "메타종아황산나트륨", "치자황색소" ],
    "origin" : "philipine"
}

for key in dictionary:
    # 키를 제외하고 값만 출력
    print("값 : ", dictionary.get(key))

# 딕서너리의 특정 값 출력
print("ingredient : ", dictionary["ingredient"])
print("ingredient[1] : ", dictionary["ingredient"][1])

# 딕셔너리에 값 추가 / 제거
dictionary["price"] = 5000
print(dictionary)

del dictionary["price"]
print(dictionary)

# 빈 공간으로 딕셔너리 선언
dictionary_a = {}
print("요소 추가 이전 : ", dictionary_a)

# 요소 추가
dictionary_a["name"] = "새로운 이름"
dictionary_a["head"] = " 새로운 정신"
print("요소 추가 이후 : ", dictionary_a)

# 딕셔너리 내부의 키 확인
key = input("> 접근하고자 하는 키: ")
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

value_g = dictionary.get("this is not key")     # 딕셔너리에 존재하지 않는 키값 탐색
print("value_g = ", value_g)                    # 없는 값은 None으로 출력이 된다

# 확인문제
numbers = [1, 2, 6, 8, 4, 3, 2, 6, 8, 9, 1, 1, 9, 2, 3, 5, 7, 3]
counter = {}

