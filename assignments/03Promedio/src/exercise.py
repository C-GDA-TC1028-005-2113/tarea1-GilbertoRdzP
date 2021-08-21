def main():
    #escribe tu código abajo de esta línea
    import math
    promedio = []

    promedio.append(int(input("Calificación de la materia: ")))
    promedio.append(int(input("Calificación de la materia: ")))
    promedio.append(int(input("Calificación de la materia: ")))
    promedio.append(int(input("Calificación de la materia: ")))

    average = math.fsum(promedio)/len(promedio)

    print(f"El promedio es: {average}")




if __name__ == '__main__':
    main()
