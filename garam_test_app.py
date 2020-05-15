# 마지막 테스트 파이썬
import json                   # json 파일 읽기

dic_mcu = []

# print(dic_mcu)
# with open("./data/mcu_movies.json", "w", encoding="UTF-8") as mcu_list:
#   json.dump(dic_mcu, mcu_list, ensure_ascii=False)

with open("./mcu_movies.json", "r", encoding="UTF-8") as mcu_list:
  dic_mcu = json.load(mcu_list)


# 문제 1번
# 페이즈가 1인 마블 시네마틱 유니버스 영화면 뽑기

for i in range(len(dic_mcu)):
  if "페이즈1"  in dic_mcu[i].get("시리즈"):
    print("{} ( {} )".format(dic_mcu[i].get("영화명"), dic_mcu[i].get("개봉일")))
  else :
    pass

# print(dic_mcu)


# 문제 2번
# 박스오피스가 450000000 이상인 영화들의 감독이름 리스트와 전체 합계금액, 평균 박스오피스 구하기

director = []
money = []

for i in range(len(dic_mcu)):
  if 450000000 <= dic_mcu[i].get("박스오피스"):
    director.append(dic_mcu[i].get("감독"))
    money.append(dic_mcu[i].get("박스오피스"))

director = list(set(director))

print("감독 리스트 : ", director)
print("총 박스오피스 합계 ＄ {0:,}".format(sum(money)))
print("평균 박스오피스 ＄ {0:,}".format(int(sum(money) / len(money))))