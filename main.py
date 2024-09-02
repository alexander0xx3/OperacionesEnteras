class CalculadoraMCD:
    def __init__(self, num1, num2):
        """Inicializa los números para calcular el MCD."""
        self.num1 = num1
        self.num2 = num2

    def calcular_mcd(self):
        """Calcula el MCD usando el método de divisiones sucesivas."""
        a, b = abs(self.num1), abs(self.num2)
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):
        """Devuelve una representación en cadena del cálculo del MCD."""
        return (f"Para los números {self.num1} y {self.num2}, "
                f"el MCD es {self.calcular_mcd()}.")


def main():
    print("Calculadora del Máximo Común Divisor (MCD) usando divisiones sucesivas.")

    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
        return

    calculadora = CalculadoraMCD(num1, num2)
    print(calculadora)


if __name__ == "__main__":
    main()
