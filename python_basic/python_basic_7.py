# 문제 7번

# 두 개의 문자열 A 와 B 한 개의 정수 n을 입력받아서 A에 B를 연결하고,
# 변경된 문자열 A에서 n개의 문자를 B에 복사한 후 A와 B를 출력하는 프로그램을 작성하시오(1<=n,A,B<=100)

# *입력 예: banana apple 3

# *출력 예:
#     -bananaapple
#     -banle

# *입력 예2 : orange watermelon 5

# *출력 예2:
#     -orangewatermelon
#     -orangmelon



A = input("문자열을 입력하세요 : ")
B = input("문자열을 입력하세요 : ")
n = int(input("정수를 입력하세요 : "))

print(A+B)
print(A[:n]+B[n:])