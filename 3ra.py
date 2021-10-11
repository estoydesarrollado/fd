nombre = input("digite su nombre: ")
print("hola ", nombre, " bienvenido")
#tema de la clases 7
n1 = int(input('introduce n1: '))
n2 = int(input('introduce n2: '))
print(type(n1))
print('la suma de los numeros es: ', n1 + n2)
print('la suma de los numeros es: {}'.format(n1+n2))
print('la suma de ', n1, ' y ', n2, 'es', n1+n2)
print('la suma de {} y {} es {}'.format(n1, n2, n1+n2))
print(f'la suma de {n1} y {n2} es {n1+n2}')
#ejemplo de como usar condicionales, primer ejemplo usando if
a = int(input('¿cuantos años tiene tu computador?: '))
if a >= 0 and a <= 2:
    print('tu computador es nuevo')
    print ('puedes continuar con tu PC')
print('-'*6)
edad = int(input('Digite la edad de la persona: '))
#Condicional elif
if edad < 16 :
    print('Todavia no puede conducir')
elif edad < 18 :
    print('puede obteneer un permiso para conducir')
elif edad < 70 :
    print('puede obtener la licencia estandar')
else:
    print('requiere de una licencia especial')

"""
creando menus dentro de python, 
entrenamiento de condicionales con 
caracteristicas especiales(metodos)str
"""
menu = """
Bienvenidos al restro de usuarios, llene
los campos que usted prefiera a continuacion
seleccionando un numero del 1 al 3:

[1] Digitar su Nombre
[2] Digitar su edad
[3] Digitar su correo electronico
"""
#python es un leguaje orientado a objetos
print(menu)
#variable opcion(objeto)
opcion = input('Digita una opcion entre 1 y 3: ')
if opcion == '1':
# == : operador de comparacion, =: operador de asignacion.
    nombre = input('Digita tu nombre: ')
    #print(nombre.isnumeric())->true, print(nombre.isalpha())->false.
    if nombre.isalpha() == true: 
        print('Tu nombre es {}'.format(nombre))
    else:
        print('Has digitado un nombre no valido...')

    print('Tun nombre es {}'.format(nombre))
elif opcion == '2':

    #pass: declaración null que se usa generalmente como marcador de posición.
    edad = input('Digita tu edad: ')
    #print(nombre.isnumeric())->true, print(nombre.isalpha())->false.
    if edad.isnumeric() == true:
        print('Tu edad es {}'.format(edad))
    else:
        print('Has digitado numero no valido...')
elif opcion == '3':
    email = input('Digita tu email: ')
    """
    email = 'cae@gmail.com'
    print(email.find('@'))->3:posicion
    print(email.find('.'))->posicion 9
    email = 'caegmail.com' : sin @
    print(email.find('@'))-> -1:porque no encontro @
    tambien no es necesario en : if nombre.isalpha() == true:, el ==true
    """
    if email.find('@')>=0 and email.find('.')>=0:
        print('Tu email es {}'.format(email))
    else:
        print('Has digitado un email no valido...')
else:
    print('debes digitar un numero entre 1 y 3')
    print('---'*20)

    
