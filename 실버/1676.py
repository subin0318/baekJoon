# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# k=1
# count=0

# for i in range (1,11):
#     k *= i

# k= 368800

# while k > 0 :
#     k %= 10
#     if k % 10 != 0 :
#        count +=1

# print(count)
          

# 120 12 * 10  3628800   36288 * 10 * 2 


j = int(input())
k=1
count = 0

for i in range (1,j+1):
    k *= i


while k % 10 == 0:
    count += 1
    k //= 10

print(count)