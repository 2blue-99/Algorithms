from operator import index


data = []
for _ in range(8):
    data.append(input(""))

count=0

for rowIndex, row  in enumerate(data):

    if (rowIndex+1) % 2 == 1: ##하얀판 먼저라면

        for index, gap in enumerate(row):
            if (index+1) % 2 == 1 and gap == "F": ## 하얀 먼저에서 하얀칸이라면
                count+=1

    else: ##검정판 먼저라면
        for index, gap in enumerate(row):
            if (index+1) % 2 == 0 and gap == "F": ## 컴정칸 먼저에서 하얀칸이라면
                count+=1

print(count)


