# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다. 각 방법은 세 정수 i j k로 이루어져 있으며, 
# i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다. 
# 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)
# 도현이는 입력으로 주어진 순서대로 공을 넣는다.

# 5 4 5개의 바구니를 4번 작업한다
# 1 2 3
# 3 4 4
# 1 4 1
# 2 2 2

# 1 2 1 1 0

# n,m = map(int,input().split())
# a=[0]*n 

# for b in range (m):
#     i,j,k=map(int,input().split())
 
# a=[0,0,0,0,0] # 0 , 1, 2, 3, 4 index 기준  2 -> index + 1

# i,j,k = map(int,input().split())

# print()

# a=[0,0,0,0,0]

# a[:3] = "3"

# print(a)

# a = [0, 0, 0, 0, 0]

# for i in range(0,4):  # 인덱스 0부터 3까지
#     a[i] = 1

# print(a)  # 바꾸는법

# 5 4 5개의 바구니를 4번 작업한다
# 1 2 3
# 3 4 4
# 1 4 1
# 2 2 2

# 1 2 1 1 0

# for i in range(0,4):  # 인덱스 0부터 3까지
#     a[i] = 1

n,m=map(int,input().split()) ## 5 4 입력
a=[0]*n # 5 * a[0] = [0,0,0,0,0]

for _ in range (m) : # m 까지 실행
    i,j,k=map(int,input().split()) # i , j , k 입력 
   
    for c in range (i-1,j) :
         # 1 부터 2 까지 배열의 값을 바꾸고 싶은면 (0 ~ 1) 인덱스 기준 이기에 i-1 해주면 된다 0 ~ 2 까지 이니 0 ~ 1 까지 출력된다
        a[c]=k # 0 ~ 1 까지 입력된 K 로 바꿔진다 

for d in a:
    print(d,end=" ") # 출력  그러나 *a 를 하면 한번에 출력이 된다 