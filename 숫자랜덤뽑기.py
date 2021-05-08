import random
a=random.randint(1,100)
i=0
o=int(input("기회 입력"))
while True:
    b = int(input("자연수 입력:"))
    i=+1
    if a==b:
        print("정답입니다")
        break
    elif a<b:
        print("입력하신 숫자가 더 높습니다")
        print("횟수: "i)
    elif a>b:
        print("입력하신 숫자가 더 낮습니다")
        print("횟수: "i)
    elif i==o:
        break
