def ingresar_evaluacion():
    while True:
        # Solicitar al usuario que ingrese una calificación del 1 al 5
        print('Por favor ingrese una calificación en una escala del 1 al 5')
        punto = input()
        if punto.isdecimal():  # Verificar si la entrada es un número decimal
            punto = int(punto)
            if 1 <= punto <= 5:  # Verificar si la calificación está dentro del rango válido
                # Solicitar al usuario que ingrese sus comentarios
                print('Ingrese sus comentarios')
                comentario = input()
                # Crear el registro con la calificación y comentario y escribirlo en el archivo
                registro = f'Punto: {punto} . Comentario: {comentario}'
                with open("data.txt", 'a') as archivo:
                    archivo.write(f'{registro}\n')
                break
            else:
                # Informar al usuario que debe ingresar un valor entre 1 y 5 si está fuera de rango
                print('Por favor ingrese un valor entre 1 y 5')
        else:
            # Informar al usuario que debe ingresar un número válido si no es decimal
            print('Por favor ingrese el número de puntos de evaluación')

def verificar_resultados():
    # Mostrar todos los resultados almacenados en el archivo data.txt
    print('Resultados hasta el momento:')
    with open("data.txt", "r") as archivo_lectura:
        print(archivo_lectura.read())

def menu_principal():
    while True:
        # Mostrar el menú principal y solicitar al usuario que seleccione una opción
        print('Por favor seleccione el proceso que desea realizar')
        print('1: Ingresar puntos de evaluación y comentarios')
        print('2: Verificar los resultados hasta el momento')
        print('3: Terminar')
        num = input()

        if num.isdecimal():  # Verificar si la entrada es un número decimal
            num = int(num)
            if num == 1:
                # Llamar a la función para ingresar evaluaciones si el usuario elige la opción 1
                ingresar_evaluacion()
            elif num == 2:
                # Llamar a la función para verificar resultados si el usuario elige la opción 2
                verificar_resultados()
            elif num == 3:
                # Informar al usuario que el programa terminará si elige la opción 3
                print('Terminación.')
                break
            else:
                # Informar al usuario que debe elegir una opción válida si no es 1, 2 o 3
                print('Por favor ingrese 1, 2 o 3')
        else:
            # Informar al usuario que debe ingresar una opción válida si no es un número decimal
            print('Por favor ingrese 1, 2 o 3')

if __name__ == "__main__":
    # Iniciar el programa ejecutando el menú principal
    menu_principal()
