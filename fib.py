# Calcula a sequência de Fibonacci (sqn)
n = int(input("n: "))
def fib_teste(n):
    x, y = 1, 1
    fib =[]
    for _ in range(n):
        fib.append(x)
        x , y = y, x + y
    return fib

fib_teste(n)
#Tive que sair mais cedo da aula, por isso só mandei agora
    
