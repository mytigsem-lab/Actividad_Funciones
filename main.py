# Función para calcular el promedio de tres notas
def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

# Programa principal
print("=== PROMEDIO DE TRES NOTAS ===")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

resultado = calcular_promedio(nota1, nota2, nota3)

print(f"El promedio es: {resultado:.2f}")