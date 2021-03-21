# 문제 7번

# 직사각형의 가로와 세로의 길이를 정수형 값을 변수에 담고,
# 가로의 길이는 5 증가시키고 세로의 길이는 2배하여 저장한 후
# 가로의 길이 세로의 길이 넓이를 차례로 출력하는 프로그램을 작성하시오.

# *입력 예: 20 15 (앞에 입력된 값이 가로, 뒤에 입력된 값이 세로 길이)
# *출력 예:

#     -width = 25
#     -length = 30
#     -area = 750

a = int(input("Width : "))
b = int(input("Length : "))


width = a+5
length = b*2
area = width*length

print("""
width = {0}
length = {1}
area = {2}""".format(width,length,area))


