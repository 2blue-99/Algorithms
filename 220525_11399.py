num = int(input(""))
data = list(map(int, input("").split()))
data.sort()
hap = 0
for i in range(num):
    hap = hap + sum(data[:i+1])
print(hap)