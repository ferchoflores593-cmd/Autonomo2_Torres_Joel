# Autor: Torres - Autonomo 2 - Logica y Algoritmos
# Archivo: torres-autonomo2.py

def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def obtener_estado(promedio):
    if promedio >= 7:
        return "Aprobado"
    elif promedio >= 4:
        return "Supletorio"
    else:
        return "Reprobado"

print("=== SISTEMA DE NOTAS - TORRES ===")
nombre = input("Nombre del estudiante: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

prom = calcular_promedio(nota1, nota2, nota3)
estado = obtener_estado(prom)

print(f"\nEstudiante: {nombre}")
print(f"Promedio: {prom:.2f}")
print(f"Estado: {estado}")
# Proyecto Programacion 2 - Joel Torres
# Sistema de Notas con estructuras logicas y repetitivas

def calcular_promedio(notas):
    # Calcula el promedio de la lista de notas
    return sum(notas) / len(notas)

def obtener_estado(promedio):
    # Estructura condicional para determinar si aprueba
    if promedio >= 7:
        return "Aprobado"
    else:
        return "Reprobado"

def main():
    print("=== SISTEMA DE NOTAS - TORRES ===")
    nombre = input("Nombre del estudiante: ")
    
    notas = []
    # Estructura repetitiva (bucle) para pedir 3 notas con validacion
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Nota {i} (0-10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Error: La nota debe ser entre 0 y 10")
            except ValueError:
                print("Error: Ingresa solo numeros")

    promedio = calcular_promedio(notas)
    estado = obtener_estado(promedio)

    print("\n--- RESULTADO ---")
    print(f"Estudiante: {nombre}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")

# Ejecucion principal
main()
