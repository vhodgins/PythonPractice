fact = 1
l = 25
while l > 0:
    fact = fact * l
    l -= 1
print(fact)

b = 0
h = fact

while h % 2 == 0:
    b += 1
    h = h // 2
    print(h)

print(b)