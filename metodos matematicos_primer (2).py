import math

x = 0.3 * math.pi
valorVerdadero = math.exp(x)
print(f"Valor verdadero: {valorVerdadero}")


def cos_maclaurin(x, tolerancia=0.0000005):
    valorAproximado = 1
    valorAproximadoanterior = valorAproximado
    errorNormalizado = 1
    n = 0
    while abs(errorNormalizado) > tolerancia:
        n += 1
        valorAproximado += (-1)**n * x**2*n / (math.factorial(2*n))
        errorVerdadero = valorVerdadero - valorAproximado
        errorRelativo = (errorVerdadero / valorVerdadero) * 100
        errorNormalizado = ((valorAproximado - valorAproximadoanterior) /
                            valorAproximado) * 100
        valorAproximadoanterior = valorAproximado
    return n, errorVerdadero, errorRelativo, errorNormalizado, valorAproximado


nTerms, errorV, errorR, errorN, valorAprox = cos_maclaurin(x)

print(f"Resultados de la ejecucion: Error aproximado {valorAprox},"
      f" error verdadero {errorV} %, el error relativo {errorR} %"
      f" y el error normalizado {errorN} %")
print(f"Número de términos necesarios: {nTerms+1}")
