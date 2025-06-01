# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.


# 1. 조건 O이 연속적이면 점수도 연속적으로  같이 오른다 

# a="OOXXOXXOOO"


# k=0 #  연속
# score=0 # 총 점수



# for i in range(len(a)):

#     if a[i] =="O" :
#         k +=1
#         score += k
#     elif a[i] == "X" :
#         k = 0
#         score += k

# print(score) # 구조완성


execution = int(input()) # 실행 횟수
consecutive= 0 # 연속 판단
score=0 # 총 점수 

for _ in range (execution):
    
    consecutive = 0  # 한번 실행된후 다시 초기화 
    score = 0       
   
    result=input()
   
    for i in range (len(result)):
        if result[i] =="O" :
            consecutive +=1
            score += consecutive
        elif result[i] == "X" :
                consecutive = 0
                score += consecutive
    
    
    print(score)