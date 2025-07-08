# 수 찾기

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# 1
# 1
# 0
# 0
# 1

# import sys

# N = int(sys.stdin.readline())
# a= list(map(int,sys.stdin.readline().split()))
# P = int(sys.stdin.readline())
# b =[0] * P
# c = list(map(int,sys.stdin.readline().split()))



# array = [1, 2, 3, 4, 4, 6, 8, 9]
# x = 4

# print(bisect_left(array, x)) # 3
# print(bisect_right(array, x)) # 5


from bisect import bisect_left
import sys

N = int(sys.stdin.readline())
a= list(map(int,sys.stdin.readline().split()))
a.sort()
P = int(sys.stdin.readline())
c = list(map(int,sys.stdin.readline().split()))


for number in c :
    
    idx = bisect_left(a, number)
    
    if idx < len(a) and a[idx] == number:
        print(1)
    
    else :  print(0)
 

