for i in range(len(a)):
    
    if a[i] == "*":
        continue
    
    k += 3 * int(a[i]) if i % 2 != 0 else int(a[i])
    
       
result = 10 - (k % 10)

print(result)
