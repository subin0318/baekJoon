# 큐

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 15
# push 1 -> 값을 넣는것
# push 2 -> 값을 넣는것
# front -> 큐의 가장 앞에 있는 정수를 출력한다
# back -> 큐의 가장 뒤에 있는 정수를 출력한다
# size -> 정수의 갯수를 출력한다
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# front

# 1 -> 맨 앞에 있는 값 
# 2 -> 맨 뒤에 있는 값
# 2 -> 정수의 갯수
# 0 -> 큐가 비어있으면 1, 아니면 0
# 1 -> pop (큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력) 없으면 -1
# 2 -> pop (큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력) 없으면 -1
# -1 -> pop (큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력) 없으면 -1
# 0 -> size
# 1 -> empty 큐가 비어있으면 1, 아니면 0을 출력한다.
# -1 -> pop 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다 없으면 -1
# 0 ->  empty  큐가 비어있으면 1, 아니면 0을 출력
# 3 -> front  맨 앞에 있는 값 출력

# 구현 해야할 기능
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.



# 문자열과 숫자가 같이 있을떄 숫자만 값을 얻고 싶을때 
# text = "push 1"
# number = ""
# for char in text:
#     if char.isdigit():
#         number += char
# print(int(number))


# N = input()

# if "push" in N :
#     print(1)


# push 값을 받는법

# import sys

# 표준 입력을 더 빠르게 받기 위해 sys.stdin.readline 사용
# 대량의 입력을 처리할 때 유용합니다.
# input = sys.stdin.readline

# 예시 입력: "push 10"
# command_line = input().split() # ['push', '10']

# command = command_line[0] # 'push'

# if command == "push":
#     value = int(command_line[1]) # '10'을 정수 10으로 변환
#     print(f"받은 명령어: {command}, 받은 값: {value}")
#     # 여기에 큐에 값을 추가하는 로직을 작성하면 됩니다.


number_list=[]
result = []


# push X: 정수 X를 큐에 넣는 연산이다.

def push(x) :
    return number_list.append(x)

# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

def pop() :
    if len(number_list) > 0 :
        return number_list.pop(0)
    else : return -1

# size: 큐에 들어있는 정수의 개수를 출력한다.

def size() :
    return len(number_list)

# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
def empty():
    if len(number_list) > 0 :
        return 0
    else : return 1

# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

def front():
    if len(number_list) > 0 :
        return number_list[0]
    else : return -1



# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

def back():
     if len(number_list) > 0 :
        return number_list[-1]
     else : return -1



# 초기 단계
# import sys
# input = sys.stdin.readline

commands = {
    
    "push" : push,
    "pop"  : pop,
    "size" : size,
    "empty": empty,
    "front": front,
    "back" : back,
}


N=int(input())

for _ in range (N):
   
   command = input().split() # 6가지 명령을 받는 변수
   
   if command[0] == "push":
    push(int(command[1]))

   else : 
    value=commands[command[0]]()
    result.append(value)


print(*result, sep="\n")