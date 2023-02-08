# Script para identificar los multiplos de un rango de numeros
# con una condicion extra para que se cierre el programa

# no es necesario inicializar variables, por lo que se inicia el for

for i in range(100, 200):
    # dentro del for va el if que indica las condiciones
    if i % 3 == 0: 
            print(i, end=", ")
    # este if indica la condicion del conteo, para este caso el programa rompe en 183
    if i == 183:
        break
        
print("Fuera de rango") # este print no aplica, solo esta puesto para una futura actualizacion      