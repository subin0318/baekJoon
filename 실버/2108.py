# 통계학

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값 (최빈값 중 두 번째로 작은 값)
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이


# [2,4,6,8] ,[1, 3, 8, -2, 2] 예시값
# number_list = [1, 3, 8, -2, 2]

# number_list.sort()


# print(f'number_list 의 값: {number_list}' )

# # 산술 평균

# arithmetic = sum(number_list) //len(number_list)
# # print(arithmetic)


# # 중앙값

# if len(number_list) % 2  != 0 :
#     print(number_list[(len(number_list) // 2)])
    
# else : print((number_list[(len(number_list) // 2)-1]+number_list[(len(number_list) // 2)])//2)

# 최빈값

# mode = {}

# number_list = [1, 3, 8, -2,1,3]

# number_list.sort()


# for i in number_list:
#     mode[i] = number_list.count(i)

# sorted_mode = [key for key, value in mode.items() if value == max(mode.values())]

# sorted_mode.sort()

# print(sorted_mode)

# if len(sorted_mode) % 2  != 0 :
#     print(sorted_mode[(len(sorted_mode) // 2)])
    
# else : print((sorted_mode[(len(sorted_mode) // 2)-1]))


#  범위
# a= [1, 3, 8, -2, 2]
# print(max(a)-min(a))

import sys 


N = int(sys.stdin.readline())
number_list = [int(sys.stdin.readline()) for _ in range(N)]
mode = {}
result=[]

    
# 산술평균 - 1
arithmetic = round(sum(number_list) / N)
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

# 최빈값 리스트 뽑기
max_count = max(mode.values())
sorted_mode = sorted([key for key, value in mode.items() if value == max_count])


if len(sorted_mode) > 1: # 최빈값이 두개일떄
    result.append(sorted_mode[1])
else:
    result.append(sorted_mode[0])


# 범위
result.append(max(number_list)-min(number_list))


print(*result, sep='\n')








