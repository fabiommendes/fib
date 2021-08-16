# Calcula a sequência de Fibonacci (sqn)
n = int(input("n: "))
x, y = 1, 1
fibonacci =[]
for _ in range(n):
    
    fibonacci.append(x)
    x , y = y, x + y
print (fibonacci)    
    
