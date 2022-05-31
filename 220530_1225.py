gap1, gap2 = input("").split()

List1 = list(gap1)
List2 = list(gap2)

List1 = list(map(int, List1))
List2 = list(map(int, List2))

print(sum(List1) * sum(List2))
