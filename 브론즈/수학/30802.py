# 웰컴 키트
# 첫 줄에 참가자의 수 N이 주어집니다.
# 둘째 줄에 티셔츠 사이즈별 신청자의 수 
# S, M, L, XL, XXL, XXXL 이 공백으로 구분되어 주어집니다
# 셋째 줄에 정수 티셔츠와 펜의 묶음 수를 의미하는 정수 
# T와 P가 공백으로 구분되어 주어집니다

# 출력
# 23 (참가자 수)
# 3 1 4 1 5 9 = N (23) (사이즈별 신청자 수)
# 5 7 (티셔츠와 펜의 묶음 수)

# 결과
# 7 (티셔츠 최소 주문)
# 3 2 (펜을 P 자루씩 최대 몇 묶음 주문)


# N=int(input())
# L= list(map(int, input().split()))
# T , P = map(int, input().split())

# a=[3,1, 4, 1, 5, 9]
# k=0

# for i in range (len(a)):
#     if a[i] % 5 == 0 :
#         k += a[i] // 5
#     else : 
#         k += (a[i] // 5) + 1

# print(k)

N=int(input())
L= list(map(int, input().split()))
T , P = map(int, input().split())

k=0

for i in range (len(L)):
    if L[i] % T == 0 :
        k += (L[i] // T)
    else : k += (L[i] // T) + 1

print(k)
print(N//P , N%P)

