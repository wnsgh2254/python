# 문제 1

# -1야드(yd)는 91.44cm이고 1인치(in)는 2.54cm이다.
# -2.1야드와 10.5인치를 각각 cm로 변환하여 다음 형식에 맞추어 소수 첫째자리까지 출력하시오.
# -출력 예:

#     * 2.1yd = 192.0cm
#     * 10.5in = 26.7cm



yad = float(input("숫자(yad)를 입력하세요 : ")) 
inch = float(input("숫자(inch)를 입력하세요 : ")) 



print(str(yad)+"yd","=" , str(round(yad*91.44, 1))+"cm")
print(str(inch)+"in","=" , str(round(inch*2.54, 1))+"cm")

