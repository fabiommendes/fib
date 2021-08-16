# Calcula a sequência de Fibonacci (sqn)
n = int(input("n: "))
fib =[1,1]
for i in range(len(fib),n):
    fib.append(fib[i-2] + fib[i-1])
print (fib)    
    
