# 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

T=int(input())
b=[]

for _ in range (T) :
    a=list(input())
    b.append(a[0]+a[len(a)-1])
    

print(*b , sep="\n")