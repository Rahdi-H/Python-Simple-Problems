i = 1234
sum = 0
while i > 0:
    sum += i % 10
    i = i // 10
print(sum)