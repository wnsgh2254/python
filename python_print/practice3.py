# 문제 3

# 두 개의 정수를 변수에 각각 담고, 다음과 같이 4가지 관계연산자의 결과를 출력하시오.
# 입력 예: 4 5 
# 출력 예 :
#     *4>5 --0
#     *4<5 --1
#     *4>=5 --0
#     *4<=5 --1


a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

if a <= b:
    print("""
    {0}>{1} --0
    {0}<{1} --1
    {0}>={1} --0
    {0}<={1} --1""".format(a,b))
elif a >= b:
    print("""
    {0}<{1} --0
    {0}>{1} --1
    {0}<={1} --0
    {0}>={1} --1""".format(a,b))
