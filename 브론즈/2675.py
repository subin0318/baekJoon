# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다

# 3 ABC
# AAABBBCCC

# a="abc"
# print(a*3)

# 2
# 3 ABC
# 5 /HTP

# AAABBBCCC
# /////HHHHHTTTTTPPPPP

# a=list(input())
# b=""

# for i in range (len(a)) :
#     b += a[i]*3

# print(b)

# 2
# 3 ABC
# 5 /HTP

# AAABBBCCC
# /////HHHHHTTTTTPPPPP

a = int(input())
k = []

for i in range(a):
    m, s = input().split()
    b = ''
    
    for j in s:
        b += j * int(m)
        
    k.append(b)

print(*k)
