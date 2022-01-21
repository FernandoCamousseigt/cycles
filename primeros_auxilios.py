respuesta = input('responde estimulos? y/n:  ')

if respuesta == 'y':
    print('esta sano')

else:
    print('abrir la via aerea')
    respuesta = input('¿respira? y/n:  ')

    if respuesta == 'y':
        print('Permitirle posicion de suficiente ventilacion')

    else:
        print('Administrar 5 ventilaciones y llamar ambulancia')

        while respuesta !='y':  #or == 'n':
            respuesta = input('¿esta vivo? y/n:  ')
            if respuesta == 'y':
                print('Reevaluar a la espera de la ambulancia')
            else:
                print('Administrar compresiones')
            respuesta = input('¿llego la ambulancia? y/n: ')
