import sys
input=sys.stdin.read()
a = input()
k = {}

for char in a:
    if char in k:
        k[char] += 1
    else:
        k[char] = 1

max_value = max(k.values())
j = ""

for key, value in k.items():
    if value == max_value:
        j += key

# 문자 정렬
j = ''.join(sorted(j))

print(j)



