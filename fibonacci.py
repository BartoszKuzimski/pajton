fibo = [0,1]
# F(X) = F(x-1) + F(x-2)

for i in range(8):
    sum = fibo[-1] + fibo[-2]
    fibo.append(sum)

print(fibo)