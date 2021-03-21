# 문제 2

# 문자열을 입력받은 뒤 그 문자열을 이어서 두 번 출력하는 프로그램을 작성하시오.
# 문자열의 길이는 100 이하이다.

#     *입력 예:ASDFG
#     *출력 예:ASDFGASDFG


string = input("문자열을 입력하시오 : ")



if len(string) > 50:
    print("글자수가 100을 넘어갑니다.")
else:
    print(string*2)