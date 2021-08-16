# Calcula a sequência de Fibonacci (sqn)
n = int(input("n: "))
x, y = 1, 1
fib =[]
for _ in range(n):
    fib.append(x)
    x , y = y, x + y
print (fib)    
# Gustavo aqui
    
