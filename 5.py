palavra_digitada = input("Digite a palavra que vai ser invertida: ")

def inverter_palavra(palavra):
    palavra_invertida = ""
    i = len(palavra) - 1  
    while i >= 0:
        palavra_invertida += palavra[i]  
        i -= 1  
    return palavra_invertida

palavra_invertida = inverter_palavra(palavra_digitada)
print(f"String original: {palavra_digitada}")
print(f"String invertida: {palavra_invertida}")
