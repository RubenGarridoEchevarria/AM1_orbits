
# Código que resuelve el factorial

f=1
n=4

for i in range(1, n+1):

        f=f*i

print (f)

# Resolución usando el paradigma funcional

def factorial(n):
        
        if n==1:
                return 1
        
        else:  return factorial(n*(n-1))

