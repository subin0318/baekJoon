# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.


# a=int(input())
# c=[]

# for i in range (a):
#     b=input()
#     c.append(b)

# c.sort()
# print(c)

# arr = [6, 5, 6, 4, 4, 1, 1, 2, 3, 9, 8, 7, 9, 8, 7]
# result = [] # 중복 제거된 값들이 들어갈 리스트

# for value in arr:
#     if value not in result:
#         result.append(value)

# print(result)


# list = ["but", "i", "wont", "hesitate", "no", "more", "no", "more", "it", "cannot", "wait", "im", "yours"]
# sorted_list = sorted(list,key=len,reverse=True)	# 문자열의 길이순으로 내림차순 정렬
# result = []

# for value in sorted_list :
#     if value not in result:
#        result.append(value)
       

# print(*result[::-1],sep="\n")


# a=int(input())
# list=[]


# for _ in range (a):
#     b=input()
#     list.append(b)
#     sorted_list = sorted(list,key=len,reverse=True)
    


# numbers = ["but", "i", "wont", "hesitate", "no", "more", "no", "more", "it", "cannot", "wait", "im", "yours"]
# sorted_list = sorted(numbers,key=len,reverse=True)
# print(sorted_list)


# list = ["but", "i", "wont", "hesitate", "no", "more", "no", "more", "it", "cannot", "wait", "im", "yours"]
# sorted_list = sorted(list,key=len,reverse=True)	# 문자열의 길이순으로 내림차순 정렬
# unique = list(set(sorted_list))
# print(*unique)


# a = ["but", "i", "wont", "hesitate", "no", "more", "no", "more", "it", "cannot", "wait", "im", "yours"]
# c = sorted(a,key=len,reverse=True)
# b = list(set(c))
# print(*b[::-1], sep="\n")

# number=int(input())
# a=[]

# for _ in range (number):
#     key=input()
#     a.append(key)

# b=list(set(a))

# c= sorted(b , key=len, reverse=True)
# print(*c[::-1], sep="\n")


# a = ["but", "i", "wont", "hesitate", "no", "more", "no", "more", "it", "cannot", "wait", "im", "yours"]

# b=list(set(a))

# b.sort()
# b.sort(key=len)

# print(b)

number=int(input())
a=[]

for _ in range (number):
    key=input()
    a.append(key)

b=list(set(a)) # set 함수는 순서 상관 없이 중복을 제거한다

b.sort() # sort 함수는 정렬할때 쓴다
b.sort(key=len) # 문자열 길이로 정렬을 한다 

print(*b, sep="\n")