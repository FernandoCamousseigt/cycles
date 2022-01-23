""" Se solicita devolver un informe resumido que exponga los meses que superan un cierto
umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor
asociado siempre y cuando superen el umbral especificado.

python mayor_a.py 40000
{'Mayo': 81000, 'Agosto': 41200, 'Noviembre': 91000} """

import sys

filtro = int(sys.argv[1])  #argv is string thats why you save it in filtro

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

#empty dictionary
resultado = {}


for m,v in ventas.items(): #take key and value #for month(m) and value(v) in sales.items() /mapping
    if filtro < v:  #comparison values with if
        resultado[m] = ventas[m] #crea noviembre(m) con el valor que este en nomviembre(m) en ventas

print(f'{resultado}')

#to run the script: terminal new and write: python mayor_a.py 40000
