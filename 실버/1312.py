# 피제수(분자) A와 제수(분모) B가 있다. 두 수를 나누었을 때, 소숫점 아래 N번째 자리수를 구하려고 한다. 
# 예를 들어, A=3, B=4, N=1이라면, A÷B=0.75 이므로 출력 값은 7이 된다.

# 소숫점을 나누는 방법
# 런타임에러
# k = "3.5714285714285716"

# q=k.split(".")

# q.pop(0)

# for i in q :
#     print(i[1])


# a,b,n = map(int,input().split())

# k = a / b

# print(k)

a,b,c = map(int,input().split())

for i in range (c+1):
    k = a//b
    a = (a % b) * 10

print(k)
