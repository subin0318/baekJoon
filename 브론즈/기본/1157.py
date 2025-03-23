# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다

# a="Mississipi"

# i= a.count(a[0])

# print(a[0])
    
# print(i)

# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# a={
     # 딕셔너리에 값 추가
# }

# b=input()
# c=input()

# a[b]=c

# print(a)

a = input()
upper_a=a.upper()

k = {}

for i in upper_a:
    if i in k:
        k[i] +=1
    else:
        k[i] =1
        

max_value = max(k.values())  
max_keys = [key for key, value in k.items() if value == max_value]  

if len(max_keys) >= 2:
    print("?")
else: print(*max_keys) 