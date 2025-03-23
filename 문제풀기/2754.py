# A+: 4.3, A0: 4.0, A-: 3.7

# B+: 3.3, B0: 3.0, B-: 2.7

# C+: 2.3, C0: 2.0, C-: 1.7

# D+: 1.3, D0: 1.0, D-: 0.7

# F: 0.0

number = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]



while True:
    C=input()
    if   C=="A+": print(number[0])
    elif C == "A0":  print(number[1])
    elif C == "A-":  print(number[2])
    elif C == "B+":  print(number[3])
    elif C == "B0":  print(number[4])
    elif C == "B-":  print(number[5])
    elif C == "C+":  print(number[6])
    elif C == "C0":  print(number[7])
    elif C == "C-":  print(number[8])
    elif C == "D+":  print(number[9])
    elif C == "D0":  print(number[10])
    elif C == "D-":  print(number[11])
    elif C == "F":   print(number[12])
    break
    
