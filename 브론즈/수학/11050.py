# 11050

# 이항계수

# 자연수 N K 가 주어질떄 이항 계수를 구하는 프로그램을 작성하시오


# 함수 활용

# def  add (a , b) :
#     return a+b


# a=int(input())
# b= int(input())

# k= add(a, b)

# print(k)

# 조건
# 팩토리얼을 N! 과 (N-K)! K! 을 구한뒤  N! // (N-K)! * K! 을 구해주면 된다
# 이번 문제는 함수를 이용해서 풀어본다


# 이항계수 변수명
# bino

import sys

def bino(N,K):
    
    r,u,k = 1,1,1
    
    for i in range (1,N+1):
        r *= i
    
    for j in range (1,K+1):
        u *= j
        
    for O in range (1,(N-K)+1):
        k *= O
        
    binomial = r // (u * k)
    
    return binomial


N,K = map(int,sys.stdin.readline().split())
result=bino(N,K)

print(result)
        