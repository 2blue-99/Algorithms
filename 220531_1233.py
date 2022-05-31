num1, num2, num3 = map(int, input("").split())
# num1=3
# num2=2
# num3=3
gapList=[]
dap={}
count=0
for x in range(1,num1+1):
    for y in range(1,num2+1):
        for z in range(1,num3+1):
            gapList.append(x+y+z)

for i in range(3,num1+num2+num3+1):
    dap[i] = gapList.count(i)
    # count+=1

a = max(dap.values())
# print(a)
# print(dap.values(3))
for key, value in dap.items():
    if value == a:
        print(key)
        break

# print(dap)
# print(len(dap))
# if len(dap) % 2 == 0:
#     print(max(dap)-1)
# else:
#     print(max(dap))
