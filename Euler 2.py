fibo = [1, 1]
summa = 0

# Creates Fibonacci sequence
while fibo[len(fibo) - 1] < 4000000:
    i = len(fibo) - 1
    fibo.append(fibo[i] + fibo[i-1])
fibo.pop()
print(fibo)

# Takes even terms and return it's sum
for i in range(len(fibo)):
    if fibo[i]%2 == 0:
        summa += fibo[i]
print(summa)