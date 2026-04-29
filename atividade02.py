def calcular_multa(peso_total):
    limite = 125  # kg
    multa_kg = 4.0  # reais por kg excedente

    if peso_total <= limite:
        print("Peso dentro do limite permitido. Não há multa.")
        return 0.0

    excesso = peso_total - limite
    multa = excesso * multa_kg

    print(f"Excesso de {excesso} kg.")
    print(f"Multa aplicada: R$ {multa}")

    return multa
peso = float(input("Digite o peso total de peixes pescados (kg): "))
calcular_multa(peso)