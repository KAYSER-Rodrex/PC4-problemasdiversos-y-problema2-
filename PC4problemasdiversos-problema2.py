#1
n = int(input('Introduce un numero entero entre el 1 y el 10: '))
file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')
for i in range(1,11):
    f.write(str(n) + 'x' + str(i) + ' = ' + str(n * i) + '\n')
f.close()

#2
n = int(input('Introduce un numero entero entero entre el 1 y el 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try:
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())
f.close()
#3
n = int(input('Introduce un numero entero entre el 1 y el 10: '))
m = int(input('Introduce otro numero entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try:
    f = open(file_name, 'r')
except FileExistsError:
    print('No existe el fichero con la tabla del ', n)
else:
    lines = f.readlines()
    print(lines[m - 1])
#4
import re
patron = input("escriba su patron: ")
print(re.match(r'@robot', patron))

#5
tweet = "Unfortunately one of those moments wasn't a giant squid monster. \n User_mentions:2 \n likes: 9 \n number of retweets: 7"
print(re.findall(r'\d', tweet))

#6
archivo = input("introduzca su nombre de archivo ")
file_name = str(archivo) + '.txt'
f = open(file_name, 'w') 
for linea in file_name:
    linea= linea.rstrip()
    if re.search(r'/[aeiou]/',linea):
        print(linea)
#7
def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None
emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    if re.match(emails, example):
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))

#8
regex = r"[0-9]{16}|(([0-9]{4}\s){3}[0-9]{4})|(-([0-9]{4}\s){3}[0-9]{4})(.)\1{4}"
tarjetas=['4123456789123456','5123-4567-8912-3456','61234-567-8912-3456','4123356789123456','5133-3367-8912-3456','5123 - 3567 - 8912 - 3456']
for example in tarjetas:
    if re.match(regex, example):
        print("valid".format(tarjeta_example=example))
    else:
        print("invalid".format(tarjeta_example=example))
    

        
