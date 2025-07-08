# 수 정렬하기 3

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.



import sys

N=int(sys.stdin.readline())

number_list=[0] * N

for i in range (N) :
    number = int(sys.stdin.readline())
    number_list[i] = number

number_list.sort()

print(*number_list, sep="\n")

