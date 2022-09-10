num1 = 28
num2 = 12
hcf = 0
for i in range(1, num2 + 1):
    if num1 % i == 0 and num2 % i == 0 :
        hcf = i

print(hcf)