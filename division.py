def dividir(a, b):
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("No se puede dividir por cero.")