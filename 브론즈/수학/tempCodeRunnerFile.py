import sys

T_list = []

T = sys.stdin.readlines()

for line in T:
    k = int(line.strip()) 
    T_list.append(k)

print(len(T_list)+1)       
print(sum(T_list)-1)       