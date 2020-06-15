# 구문(syntex) 오류 및 예외 처리 학습

# 예외 처리 try ~ except
try:
    radius = int(input("정수 입력 > "))                     # 정수가 아닌 다른 수가 입력될 경우 except 실행
      
    print("원의 반지름 : ", radius)
    print("원의 둘레 : ", 2 * 3.14159265 * radius)
    print("원의 넓이 : ", 3.14159265 * radius * radius)
    pass
except Exception as ex:
    print("잘못된 입력입니다.")                             # 에러 발생 시 실행
    pass
# else:
#     print("에러가 발생하지 않았습니다")                     # 에러가 발생 하지 않은 경우 실행
# finally:
#     print("프로그램 종료")                                 # 항상 실행


# lists = ['11', '22', '33', '44', '하이', '55']
# outputs = []

# for item in lists:
#     try:
#         float(item)
#         outputs.append(item)
#     except:                                             # 예외를 pass로 넘겨버린다.
#         pass

# print(outputs)                                          # float 형식으로 변환된 값만 출력된다.