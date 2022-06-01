height, width = map(int, input("").split())
dataList=[]

for i in range(height):
    dataList.append(list(input("")))

def checking(emptyRow):
    
    for i in range(width):
        full=0
        for k in range(height):
            if dataList[i][k] == "X":
                full=1
                break
        if full==0:
            emptyColumn = i
            break
    return emptyColumn

xCount=0
#열검사기
for row in dataList:
    if 'X' not in row:
        emptyRow = dataList.index(row)
        # print("emptyRow :",emptyRow)
        emptyColumn = checking(emptyRow)
        # print("emptyColumn :",emptyColumn)
        dataList[emptyRow][emptyColumn] = "X"
        xCount+=1
    # print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    # for i in dataList:
        # print(i)
    # print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# print("X카운트 :",xCount)

#행검사기
emptyIndex=0

for w in range(width):
    full=0
    for h in range(height):
        if "X" in dataList[h][w] :
            full=1
            break
    if full==0:
        emptyIndex = h
        dataList[h][w] = "X"

    # print("")
    # for i in dataList:
    #     print(i)




print(xCount)
