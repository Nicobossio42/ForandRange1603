numero=int(input("Ingrese su número: "))
fun=1
if numero!=0:
    for i in range(1,numero+1):
        fun=fun*i
print("Factorial:", fun)
