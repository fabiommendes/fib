# Calcula a sequência de Fibonacci (sqn)
n = int(input("n: "))
a = 1
b = 1
c = 2

for _ in range(n):
    print(a)
    print(b)
    print(c)
    a = c + b
    b = c + a
    c = a + b
    
