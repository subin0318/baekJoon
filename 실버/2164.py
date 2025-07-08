# 카드 2

# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

# 입력 6
# 출력 4

# N = 4 일 경우

# 1 , 2, 3, 4
# 3, 4, 2  
# 2,4
# 4

# 시간 초과
# N = int(input())

# a=[_ for _ in range (1, N+1)]


# while True :
#     k=a.pop(0)
#     l=a.pop(0)
#     a.insert(len(a)+1, l)

#     if len(a) == 1 :
#         break

# print(*a)



from collections import deque
import sys



N=int(sys.stdin.readline())

# 1. 큐 생성
my_queue = deque()

for i in range (1, N+1) :
    my_queue.append(i)

while len(my_queue) > 1 :
    
    item = my_queue.popleft()
    item2 = my_queue.popleft()
    my_queue.append(item2)
       


print(*my_queue)