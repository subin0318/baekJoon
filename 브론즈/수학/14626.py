# ISBN

# 이 체크기호는 일련번호의 앞에서부터 각 자리마다 가중치 1, 3, 1, 3…. 를 곱한 것을 모두 더하고, 
# 그 값을 10으로 나눈 나머지가 0이 되도록 만드는 숫자 m을 사용한다.

# 출력
# 9788968322*73

# 결과
# 2


# 홀수일때


a=list(input())

k=0


for i in range(len(a)):
    
    if a[i] == "*":
        continue
    
   
    if i % 2 != 0 :
        k+=(3*int(a[i]))
        
    
    if i % 2 == 0 :
        k+=(int(a[i]))
        

pos = a.index("*") 


if pos % 2 != 0 :
   result=(3*(k % 10)) % 10
   print(result)

else: 
    result = 10 - (k % 10)
    print(result)