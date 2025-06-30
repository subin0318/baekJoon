number_list=[1,3,8,-2,2]
number_list.sort()
mode = {}
result=[]

if len(number_list) % 2  != 0 :
    result.append(number_list[(len(number_list) // 2)])
    
else : result.append((number_list[(len(number_list) // 2)-1]+number_list[(len(number_list) // 2)])//2)

print(result)