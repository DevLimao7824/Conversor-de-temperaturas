
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def conversor():
    try:
        celsius = float(input("Digite a temperatura em Celsius (somente o número): "))
        f = celsius_para_fahrenheit(celsius)
        k = celsius_para_kelvin(celsius)

        print(f"\nTemperatura em Fahrenheit: {f:.2f}°F")
        print(f"Temperatura em Kelvin: {k:.2f}K")
    except ValueError:
        print("⚠️ Erro: Digite apenas números, sem símbolos como °C.")

conversor()