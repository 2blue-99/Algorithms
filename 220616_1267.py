num = int(input(""))

gap = list(map(int, input("").split()))

#영식은 30초 < 이면 10원씩, 30초 <= 부터 59초사이면 20원 
#민식은 60초 < 이면 15원씩, 60 <= 119  30원 청구

def Young(time):
    result = 0
    while 1:
        if time <= 0:
            break
        time = time - 29
        result += 10
    return result

def Min(time):
    result = 0
    while 1:
        if time <= 0:
            break
        time = time - 59
        result += 15
    return result

younghap = 0
minhap = 0

for i in gap:
    want = Young(i)
    want2 = Min(i)
    younghap += want
    minhap += want2

print("")
print("younghap :",younghap)
print("minhap :",minhap)
print("")

if younghap > minhap:
    print("M",minhap)
elif younghap < minhap:
    print("Y",younghap)
else:
    print("Y M",younghap)