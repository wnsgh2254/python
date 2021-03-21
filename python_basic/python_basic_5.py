# 문제 5번

# 문자열(100자 이하)을 입력받은 후 정수를 입력받아 해당위치의 문자를 제거하고 출력하는 프로그램을 작성하시오.

# *입력 예: word 3
# *출력 예: wod

word = input("문자열을 입력하세요 : ")
num = int(input("정수를 입력하세요 : "))

if len(word) > 100:
    print("문자열은 100자 이하로만 입력 가능합니다.")
elif len(word) < num:
    print("입력한 숫자는 입력한 문자열의 길이보다 클 수 없습니다.  ")
else:
    print(word.replace(word[num-1], ""))
