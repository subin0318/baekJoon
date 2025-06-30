# 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다


# 조건 찾기
# 1. 수 + 각 수의 자릿수 를 더한 합이 분해합이다
# 2. 수를 자리별로 쪼개야한다

# number = 113

# k=sum(map(int, str(number)))
    
# print(k)

K = int(input())

number = 0

while True :
    
    if number >= 1000000:
        print(0)
        break
    
    sum_number = number + sum(map(int, str(number))) # 각 자릿수를 구하고 싶을때 
    
    if sum_number == K :
        print(number)
        break
    
    number +=1
    
    