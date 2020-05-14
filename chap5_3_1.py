# 파일 쓰기 읽기 학습

# # 랜덤함수 불러오기
# import random

# hanguls = list("오그영아타영뱅이")

# # data 폴더 안에 아래 내용으로 txt 파일 쓰기(w)
# with open("./data/result.txt", "w") as f:                                    # with 를 사용하면 파일을 close 하지 않아도 된다.
#     #f.write("{}, {}, {}\n".format("이름", "몸무게", "키"))

#     for i in range(1000):
#         name = random.choice(hanguls) + random.choice(hanguls)              # hanguls list에서 랜덤으로 뽑아서 두 글자 이름으로 생성
#         weight = random.randrange(40, 100)                                  
#         height = random.randrange(150, 200)

#         f.write("{}, {}, {}\n".format(name, weight, height))


# data 폴더 안의 txt 파일 읽어오기(r)
with open("./data/result.txt", "r") as f:
    for line in f:
        (name, weight, height) = line.strip().split(",")

        if(not name) or (not weight) or (not height):                      
            continue

        bmi = int(weight) / (int(height) * int(height)) * 10000
        result = ""
        
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else :
            result = "저체중"

        print("\n".join([
            "이름 : {} ",
            "몸무게 : {} ",
            "키 : {} ",
            "bmi : {} ",
            "결과 : {}"
        ]).format(name, weight, height, bmi, result))
        print()