# 20개 이하의 문자로 이루어진 10개의 단어와 한 개의 문자를 입력받아서 마지막으로 입력받은 문자로
# 끝나는 단어를 모두 출력하는 프로그램을 작성하시오.

# *입력 예:
#     -champion
#     -tel
#     -pencil
#     -olympiad
#     -class
#     -information
#     -jungol
#     -lessom
#     -book
#     -lion
#     -l << 알파벳 l

# *출력 예:
#     -tel
#     -pencil
#     -jungol



word = []

while len(word) < 10:
    
    word.append(input("단어를 입력하세요 (문자는 20개 이하): "))

ele = input("문자를 입력하세요 : ")

for i in word:
    if i[-1] == ele:
        print(i)

