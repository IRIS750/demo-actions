def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: No se puede dividir por cero.")
        
if __name__ == "__main__":
    print(dividir(6, 2))