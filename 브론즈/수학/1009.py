# 재용이 컴퓨터 값 처리

# 1번 -> 1  
# 2번 -> 2
# 3번 -> 3
# 4번 -> 4
# 5번 -> 5
# 6번 -> 6
# 7번 -> 7
# 8번 -> 8
# 9번 -> 9
# 10번 -> 10

# k = str(9 ** 635)

# print(k[-1])

T=int(input())

for i in range (T):
    a,b=map(int,input().split())
    result = pow(a,b,10)
    # 삼항 연산자
    print(10 if result == 0 else result)
    
