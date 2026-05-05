def classificacao_imc(imc):
    if imc < 16.9:
        return "Abaixo do peso"
    elif imc < 18.5:
        return "Peso baixo"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau I"
    elif imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Processamento
imc = calcular_imc(peso, altura)
categoria = classificacao_imc(imc)

# Saída
print(f"\nSeu IMC é: {imc}")
print(f"Classificação: {categoria}")