""" PROBLEMA ULTIMO DIGITO"""

print("------------------------")
print("------ULTIMO DIGITO-----")
print("------------------------")

# input 
X = int(input("Digite el valor de X: "))

# procesing 
ultimo_digito = X % 10 
R = ultimo_digito % 2

if R == 0:
    print("El ultimo digito de " + str(X) + " es Par")

