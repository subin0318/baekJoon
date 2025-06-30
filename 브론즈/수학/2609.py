# 최소 공배수와 최대 공약수
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성

# lcm  gcd   최소공배수와 최대 공약수의 변수명


a, b = map(int, input().split())
lcm = 1 
k = 2

while k <= min(a, b) :  
    # min 을 쓰는 이유는 공약수는 두 수 중 작은 값까지만 검사하면 되기 떄문이다
    # 공약수는 두 수 중 작은 값까지만 확인하면 된다 그 이상은 둘 다 나눌 수 있는 수가 없기 떄문이다
    if a % k == 0 and b % k == 0:
        lcm *= k
        a = a // k
        b = b // k
    else:
        k += 1

gcm = lcm * a * b

print(lcm , gcm , sep="\n")


