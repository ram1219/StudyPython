try:
    number = int(input("정수 입력 : "))

    if number > 0:
        raise NotImplementedError("0보다 큼 : 구현안됨")
    else:
        raise NotImplementedError("0보다 작음 : 구현안됨")
except NotImplementedError as ex:
    print("개발자님 제발 구현좀 해놓으세요")
    print(ex)
    pass
except ValueError as 