# 문제 4

# 두 변수에 논리 값(true, false)을 각각 임의로 대입하고, 논리 합(or)과 논리 곱(and)의 결과를 
# 출력하시오.

# 입력 예: False True

# 출력 예 :
#     *논리 합:False or True =>True
#     *논리 곱:False and True =>False

a = input("True or False? : ")
b = input("True or False? : ")

if a==b:
    print("True 와 False는 각각 한번씩 입력 가능합니다.")
else:
    print("""
논리 합: {0} or {1} => True
논리 곱: {0} and {1} => False""".format(a,b))





