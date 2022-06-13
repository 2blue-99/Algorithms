A=[]
for i in range(3):
    repeat = int(input(""))
    gap = 0
    for i in range(repeat):
        data = int(input(""))
        gap = data+gap
    
    if gap>0:
        A.append("+")
    elif gap<0:
        A.append("-")
    else:
        A.append("0")

for i in A:
    print(i)
