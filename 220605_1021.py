size, wantNum = map(int, input("").split())
wantList = list(map(int, input("").split()))

List = [i for i in range(1,size+1)]
print("List:",List)
print("size, wantNum:",size, wantNum)
global count
count=0
global now
now=0



def pop():
    List.pop(now)
    print("현재 가르키는 위치 :",now)

def left():
    global now
    now+=1
    global count
    count+=1
    print("현재 가르키는 위치 :",now)
    
def reight():
    global now
    now-=1
    global count
    count+=1
    print("현재 가르키는 위치 :",now)

print("현재 위치 :",now)





# for want in wantList:

#     if want != now:
#         A=0
#         B=0
#         while want != size & (count + A):
#             A+=1
#         while want != List[count + B]:
#             B-=1
        
#         if A>=B:
#             count = count + A
#         else:
#             count = count + B

#         List.pop(count)
#         now = List[count]
#     else:
#         List.pop(count)
#         now = List[count]
                
# print(count)
        
        

        
