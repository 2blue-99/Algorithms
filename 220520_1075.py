N = int(input(""))
F = int(input(""))

gap = list(str(N))[-2:]
gap = int("".join(gap))
# print(gap)
startGap = N - gap
# print(startGap)
count=0
# quit()
while True:
    if startGap%F == 0:
        break
    count+=1
    startGap+=1
if count<10:
    print(str(0)+str(count))
else:
    print(count)