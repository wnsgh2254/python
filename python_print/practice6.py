# 문제 6번

# 두 정수를 변수 2개에 각각 담고 나눈 몫과 나머지를 다음과 같은 형식으로 출력하는 프로그램을 작성하시오.

# *입력 예: 35 10
# *출력 예: 35 / 10 = 3...5


a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

quota = a // b
remainder = a%b

print("{0} / {1} = {2}...{3}".format(a,b,quota,remainder))
