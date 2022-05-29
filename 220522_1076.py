data = {}
data["black"] = 1
data["brown"] = 10
data["red"] = 100
data["orange"] = 1000
data["yellow"] = 10000
data["green"] = 100000
data["blue"] = 1000000
data["violet"] = 10000000
data["grey"] = 100000000
data["white"] = 1000000000

oneC = input("")
twoC = input("")
threeC = data[input("")]
for index, key in enumerate(data):
    if oneC == key:
        oneC = index
    if twoC == key:
        twoC = index

print(oneC)
print(twoC)
print(threeC)
quit()
print(int(str(oneC)+str(twoC))*threeC)