# yield 키워드 학습

# 함수 생성
def test():
    print("A 지점 통과")
    yield 1                             # yield 키워드 --> 함수 내부 코드를 실행하지 않늗다.
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
# 함수 종료

# 메인
output = test()

print("D 지점 통과")
a = next(output)                        # next 함수를 이용하여 yield 키워드의 이전까지 코드를 실행한다.
print(a)                                # yield 로 설정한 값이 출력된다

print("E 지점 통과")
b = next(output)
print(b)

print("F 지점 통과")
#c = next(output)                      # 오류 발생 --> yield를 두 개만 생성한 후 앞에서 next함수를 이용해 yield를 모두 실행하였으므로 오류 발생 
                                       # yield 키워드를 사용하여 함수 내부 코드를 단계별로 실행할 수 있다.