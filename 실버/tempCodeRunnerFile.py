import sys 
input = sys.stdin.readline()


N = int(input())
number_list=[]
mode = {}
result=[]


for _ in range (N):
    number=int(input())
    number_list.append(number)
    
# 산술평균 - 1
arithmetic = sum(number_list) //len(number_list)
result.append(arithmetic)

# 중앙값  - 2
number_list.sort()

if len(number_list) % 2  != 0 :
    result.append(number_list[(len(number_list) // 2)])
    
else : result.append((number_list[(len(number_list) // 2)-1]+number_list[(len(number_list) // 2)])//2)

# 최빈값  - 3
mode = {}
for num in number_list:
    if num in mode:
        mode[num] += 1
    else:
        mode[num] = 1

sorted_mode = [key for key, value in mode.items() if value == max(mode.values())]

sorted_mode.sort()


if len(sorted_mode) > 1: # 최빈값이 두개일떄
    result.append(sorted_mode[1])
else:
    result.append(sorted_mode[0])


# 범위
result.append(max(number_list)-min(number_list))


print(*result)
