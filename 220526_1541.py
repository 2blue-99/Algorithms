data = input("").replace("+"," + ")
data = data.replace("-", " - ")
# print(data)
data = data.split()
# print(data)
for i in data:
    if i == '+' or i == '-':
        continue
    data[data.index(i)] = int(i)
print(data)
count=2
num = (len(data)-2)//2
if data[1]=="-":
    
    for i in range(count,len(data)+1,2):
        if i%4 != 0:
            hap = data[i] + data[i+2]
            data[i+2] = hap
        else:
            hap = data[i] - data[i+2]
    print(data)
    



    # for i in range(num):
    #     print(i)

    #     for i in range(2,len(data)+1,2):
    #         hap = data[i] + data[i+2]

            

# count=2
# if data[1]=="-":
#     for i in range(5, len(data),2):
#         print(data[count:i])


# print(data)
# testData = data[:]
# big = 0
# if data[1]=="-":
#     for index, i in enumerate(data[3::2]):
#         if i == "+":
#             hap = data[index-1] + data[index+1]
#             testData[index-1] = ""
#             testData[index] = ""
#             testData[index+1] = hap
#             wantIndex = index
#             if hap > big:
#                 big = hap

#         else:
#             hap = data[index-1] - data[index+1]
#             testData[index-1] = ""
#             testData[index] = ""
#             testData[index+1] = hap
#             wantIndex = index
#             if hap > big:
#                 big = hap

# big = 0
# bigIndex = 0
# for index, gap in enumerate(data,start=1):
#     if gap == "+":
#         print(index)
#         num1 = data[index-1]
#         num2 = data[index+1]
#         want = index
#         hap = num1+num2
#         if hap >= big:
#             big = hap
#             bigIndex = want
#             print(big)
#             print(bigIndex)

# print(data)

# print()
    
# if data[1] == "-":
#     for i in range(2, len(data),3):
#         num1 = data[i]
#         buho = data[i+1]
#         num2 = data[i+2]
#         if buho=="+":
#             hap = hap + num1 + num2
#         else:
#             hap = hap + num1 - num2
#     dap = data[0] - hap
#     print(dap)



