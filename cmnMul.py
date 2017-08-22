n1 = int(input("First Number: "))
n2 = int(input("Second Number: "))
cm = []
total = 0
m = n1 * n2
mcopy = n1 * n2
while mcopy < 1000:
    mcopy += m
    total += mcopy
print(total)
