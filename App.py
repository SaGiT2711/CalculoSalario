def calcular_salario(horas_trabajadas, puesto):
    # Definir las tasas de salario por hora para cada puesto
    tasas_salario = {
        "gerente": 35,
        "supervisor": 30,
        "empleado": 25
    }
    
    # Verificar si el puesto es válido
    if puesto.lower() not in tasas_salario:
        return "Puesto no válido"
    
    # Calcular el pago de las horas extra trabajadas (se puede dejar en 0)
    Pago_HEx = (horas_Extra * tasas_salario[puesto.lower()]) * 2

    # Calcular el salario basado en las horas trabajadas y la tasa de salario
    salario = (horas_trabajadas * tasas_salario[puesto.lower()]) + Pago_HEx
    
    return salario

# Ejemplo de uso
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
horas_Extra = float(input("Ingrese las horas extra trabajadas: "))
puesto = input("Ingrese el puesto del trabajador (gerente/supervisor/empleado): ")

salario = calcular_salario(horas_trabajadas, puesto)
if isinstance(salario, str):
    print(salario)
else:
    print("El salario del trabajador es:", salario)
