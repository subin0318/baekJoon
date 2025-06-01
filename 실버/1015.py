# 비내림차순으로 구하는 문제

# a = [2, 1, 3, 1]


# sorted_a = sorted((value, idx) for idx, value in enumerate(a))

# result = [0] * len(a)

# for new_idx, (value, old_idx) in enumerate(sorted_a):
#     result[old_idx] = new_idx

# print(result)  

T= int(input())

k=list(map(int,input().split()))

sort_k = sorted((vaule, idex) for idex, vaule in enumerate(k))

result = [0] * len(k)

for new_idex , (value,before_idx) in enumerate (sort_k) :
    result[before_idx] = new_idex
    
print(*result)