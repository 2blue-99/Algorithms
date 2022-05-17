num = int(input(""))
for i in range(num):
    a,b = map(int, input("").split())
    gap = a**b
    gap = list(str(gap))[-1]
    print(gap)

