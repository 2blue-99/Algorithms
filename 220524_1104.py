num, gap = map(int, input("").split())
List = []
for _ in range(num):
    List.append(int(input("")))

count=0
for i in List[::-1]:
    if gap==0:
        break
    if gap>=i:
        A = gap//i
        gap = gap - A*i
        count+=A

print(count)
    


