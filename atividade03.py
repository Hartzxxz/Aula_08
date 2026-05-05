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
