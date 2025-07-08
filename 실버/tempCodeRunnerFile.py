
from collections import Counter

a = [1, 2, 3, 2, 5, 2, 3]
c = [1, 2, 3, 4, 5]
b = []

count_a = Counter(a)

for value in c:
    b.append(count_a.get(value, 0))

print(b)