#variables
print('Calculadora python, v;2.0 funcional')
x = int(input ("Escribe la primera variable: "))
y = int(input ("Escribe la segunda variable: "))
list = ['sumar = s' , 'restar = r' , 'multiplicar = m' , 'dividir = d']
print(list)
z = input ("Escribe segun la anterior lista: ")

#codigo
if z == 's' :
    print(x+y)
    input()

if z == "r" :
    print(x-y)
    input()

if z == "m":
    print(x*y)
    input()

if z == "d" :
    print(x/y)
    input()


