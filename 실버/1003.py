# 피보나치 함수

# 조건

# 함수를 씀
# n==0 이면 "0" 을 출력함
# n==1 이면 "1" 을 출력함
# 0 과 1이 아니면 함수 매개변수값을  n-1 과 n-2 로 함
# 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 
 
# 0 이면 --> 1,0 
# 1 이면  --> 0 , 1
# 3이면  (3 - 1)   + (3 - 2) => 2 -> (2-1) + (2-2)   => (1) + (0) + (1)
# 4이면  (4-1) + (4-2) = (3) + (2)  = (1) + (0) + (1) + (1) + (0)

# T -> 몇번 실행하는지

# T = int(input())

# for _ in range (T) :

# 숏코딩 풀이
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     zero,one=1,0 # zero: 0개수, one: 1개수
#     for i in range(N):
#         zero,one = one,zero+one # zero와 one에 대해 피보나치적용
#     print(zero,one)

T=int(input()) # 몇번 처리

for _ in range (T):
   
    count_0 , count_1 = 1 , 0 # 기본값
    
    n=int(input()) 
    
    for _ in range (n): # 0이면 실행이 안된다
        count_0,count_1 = count_1,count_0 + count_1 
    # 0 일때 -> 1, 0 
    # 1일때 -> (count_1 , count_0 + count_1 ) 이 되면서 1, 0 이 0 ,1 이된다
    # 2일때 -> (count_1 , count_0 + count_1 )  되면서  (1 (count_1) , 1(count_0) + 1(count_1))
   
    print(count_0,count_1)
    
