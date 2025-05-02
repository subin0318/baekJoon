# 입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장이 주어진다. 각 줄은 최대 255글자로 이루어져 있다.

# 입력의 끝에는 한 줄에 '#' 한 글자만이 주어진다.

a=['a', 'e', 'i', 'o', 'u'] 
k=0 

while True:
    
    b=[]
    m=input()
    
    if m == "#":
        break
    
    
    for i in m:
        if i.lower() in a:
            k+=1
    
    print(k)
    k=0    
        

# a=['a', 'e', 'i', 'o', 'u']
# b=['d', 'f', 's', 'd', 'f',"a"]


# for i in b:
#     if i in a:
#         print(f"{i} 포함")




       
