# 문제 8번

# 민수와 기역이의 키와 몸무게를 각각 변수에 담고, 
# 미수가 키도 크고 몸무게도 크면 True 그렇지 않으면 False을 출력하는 프로그램을 작성하시오.

# *입력 예:
#     -150 35 (민수의 키와 몸무게 값)
#     -145 35 (가영이의 키와 몸무게 값)

# *출력 예:
#     -False


min_height = int(input("민수의 키를 입력하세요 : "))
min_weight = int(input("민수의 몸무게를 입력하세요 : "))

young_height = int(input("가영이의 키를 입력하세요 : "))
young_weight = int(input("가영이의 몸무게를 입력하세요 : "))

if min_height > young_height and min_weight > young_weight:
    print(True)
else:
    print(False)
