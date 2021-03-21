# 문제 5번

# 3개의 정수를 변수 3개에 담아 첫 번째 수가 가장 크면 True 아니면 False을 출력하고,
# 세 개의 수가 모두 같으면 True 아니면 False을 출력하는 프로그램을 작성하시오.

# *입력 예: 10 9 9
# *출력 예 : -True - False



a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))

if a > b and a > c:  # 첫 번째 조건
    print("True")
else:
    print("False")


if a == b == c: # 두 번째 조건
    print("True")
else:
    print("False")

