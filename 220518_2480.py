num1, num2, num3 = map(int, input("").split())

if num1 != num2 and num1 != num3 and num2 != num3:
    big = max(num1, num2, num3)
    print(big*100)
elif num1 == num2 == num3:
    print(10000 + num1*1000)
else:
    if num1 == num2:
        big = num1
    elif num2 == num3:
        big = num2
    else:
        big = num1
        
    print(1000 + big*100)
    