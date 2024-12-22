# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오

# a=[1,2,3,4,5,6,7,8,9,10,1]

# print(a.count(1))


# for i in range (len(a)) :
#     if a[i] != a[i] :
#        print(a[i])

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 값이 있는지 확인
# value = 5
# if value in a:
#     print(f"{value}는 리스트에 있습니다.")
# else:
#     print(f"{value}는 리스트에 없습니다.")

# for i in range (len(a)) :
#     for j in a :
#         if a[i] == j :
#             print(a[i])

# a=[1,2,3,4,5,6,7,8,9,10,1]

# print(a.count(1))

# a 배열에 1이 몇개 있는지 근데 중복은 두개 이상인까 count 값을 넣어서 2이상 인걸 출력해보자 

# a = [ 39, 40, 41, 0, 1, 2, 40, 41, 0, 1]
# b=[]
# count=0

# for i in range (len(a)) :
#     if a.count(a[i]) <= 1:
#        b.append(a[i])

# print(b)

# a=[0,0,1,2,3]
# count=0

# for i in range (len(a)) :
#     if a.count(a[i]) == 1 or a.count(a[i]) >= 2:
#        count+=1

# print(count)

# 1 입력값
# 2 
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 10 # 결과



# a=[]
# count=0

# for _ in range (10) :
#     n=int(input())
#     b=n%42
#     a.append(b)
        
# for i in range (len(a)):
#     if a.count(a[i]) == 1:
#        count+=1


# print(count)


# 42
# 84
# 252
# 420
# 840
# 126
# 42
# 84
# 420
# 126

# 39
# 40
# 41
# 42
# 43
# 44
# 82
# 83
# 84
# 85

# data = [39, 40, 41, 0, 1, 2, 40, 41, 0, 1]
# result = []

# for i in data:
# 	if i not in result:  # 해당 데이터가 없다면 추가해주고, 이미 존재한다면 넘어간다. 
#          result.append(i)

# print(len(result))

a=[]
k=[]

for _ in range (10) :
    n=int(input())
    b=n%42
    a.append(b)
        
for i in a:
    if i not in k:
         k.append(i)


print(len(k))

# 39
# 40
# 41
# 42
# 43
# 44
# 82
# 83
# 84
# 85