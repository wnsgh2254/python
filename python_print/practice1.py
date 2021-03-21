# 문제 1

# 다음 출력 예와 같이 출력되는 프로글매을 작성하시오.
# 합계와 평균은 수식을 이용하세요.
# 합계 : 세 과목의 총합
# 평균 : 세 과목의 평균
# 출력 예:

#     *kor 90
#     *mat 80
#     *eng 100
#     *sum 270
#     *avg 90

kor = int(input("국어 점수를 입력하세요 : "))
mat = int(input("수학 점수를 입력하세요 : "))
eng = int(input("영어 점수를 입력하세요 : "))
sum = kor+mat+eng
avg = sum/3
print("kor",kor)
print("mat",mat)
print("eng",eng)
print("sum",sum)
print("avg",avg)

