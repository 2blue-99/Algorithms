from dataclasses import dataclass


num = int(input(""))
data = []
dapList=""
for _ in range(num):
    data.append(list(input("")))
lengh = len(data[0])
for i in range(lengh):
    diff = 0
    compare = ""
    for k in range(num):
        gap = data[k][i]
        if compare == "":
            compare = gap
            continue

        if compare != gap:
            dapList+="?"
            diff = 1
            break
    if diff != 1:
        dapList += gap
    
print(dapList)
        

