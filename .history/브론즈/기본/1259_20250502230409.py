while True:
    a=input()
     if a == "0" : break
    # 삼항 연산자 참 if 조전 else 거지
    p= "yes" if a == a[::-1] else "no"
    print(p)
   
    