# a= 28
# k=[]

# for i in range (1,28):
#     if a % i ==0:
#         k.append(i)
        
# if 

k=[]

while True:
    a=int(input())
    
    if a == -1 :
        break
    
    for i in range (1,a):
        if a % i == 0:
            k.append(i)
                
    if sum(k) != a :
        print(a,"is NOT perfect.")
        k.clear()
        
    else: print(f"%d = {' + '.join(map(str, k))}" %a)
    k.clear()

# k = [1, 2, 3]
# print(f"6 = {' + '.join(map(str, k))}")

