# 0,1,1,2,3,5,8,

n = eval(input("Enter n: "))
t1, t2 = 0, 1
while True:
    if n > 2:
        print(str(t1) + ",", str(t2) + ",", end=" ")
        for i in range(3, n + 1):
            t3 = t1 + t2
            print(t3, end="")
            t1, t2 = t2, t3
            if i == n:
                break
            print(",", end=" ")
        break
    elif n <= 2:
        if n == 1:
            print(0)
        elif n == 0:
            print()
        elif n == 2:
            print("0, 1")
        else:
            print("Enter Positive Number !")
            n = eval(input("Enter n: "))
