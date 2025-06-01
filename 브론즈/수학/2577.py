# 조건

# A * B * C 를 계산한다
# 0부터 9까지 몇번씩 쓰였나

number_count = {
  
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0
}

a=int(input())
b=int(input())
c=int(input())

k = str(a*b*c)

for i in k :
    if i in number_count :
        number_count[i] +=1
            
for i in number_count :
    print(number_count[i])