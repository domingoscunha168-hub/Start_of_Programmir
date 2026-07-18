class cubo:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado * self.lado


def main():
    p1 = cubo(4)

    print(f'Perimetro = {p1.perimetro():.1f}')
    print(f' Area = {p1.area():.1f}')


if __name__ == "__main__":
    main()