# 스택

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


number_list=[]
result=[]

# 함수

def push(x):
    number_list.append(x)

def pop():
    return number_list.pop() if len(number_list) > 0  else -1

def size():
    return len(number_list)

def empty():
    return 1 if len(number_list) == 0   else 0

def top():
    return number_list[-1] if len(number_list) > 0   else -1


commands = {
    
    "push" : push,
    "pop"  : pop,
    "size" : size,
    "empty": empty,
    "top" : top,
}



N = int(input())

for _ in range (N):
    command = input().split()
    
    if command[0] == "push":
       push(int(command[1]))

    else : 
          value=commands[command[0]]()
          result.append(value)


print(*result, sep="\n")

