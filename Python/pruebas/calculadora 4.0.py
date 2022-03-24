#librerias
import random
#variables
print('Calculadora python, v;3.0 funcional')
while True:
    print('1=calculadora, 2=numero aleatorio, 3= numero pi')
    var_opcion = int(input ('Elige opcion: '))
    if var_opcion == 1:
        x = int(input ("Escribe la primera variable: "))
        y = int(input ("Escribe la segunda variable: "))
        list = ['sumar = s' , 'restar = r' , 'multiplicar = m' , 'dividir = d' , 'elevar (b) a (a) = e']
        print(list)
        z = input ("Escribe segun la anterior lista: ")
        
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
        
        if z == "e" :
            print(x**y)
            input()
    
    if var_opcion == 2:
        print('Elige los numeros entre los que esta el numero aleatorio')
        var_randm1 = int(input('Escribe la primera opcion: '))
        var_randm2 = int(input('Escribe la segunda opcion: '))
        print(random.randint(var_randm1, var_randm2))
        input()
        
    if var_opcion == 3:
        print('pi = 3.14159265359' )
        input()
