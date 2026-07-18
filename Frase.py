class Frase:                            
    def __init__(self, texto: str):
        self.texto = texto

    def display(self) -> None:
        print(self.summary())

    def summary(self) -> str:
        frase = self.texto
        return (
            f'A letra a aparece: {frase.count("a")} vezes na frase\n'
            f'Com espacos: {frase.isspace()}\n'
            f'Em maiuscula: {frase.isupper()}\n'
            f'esta em minuscula: {frase.islower()}\n'
            f'Com numeros: {frase.isnumeric()}\n'
            f'Com letras: {frase.isalpha()}\n'
        )

def main() -> None:
    texto = input('Informe uma frase: ').lower()
    frase_obj = Frase(texto)                        
    frase_obj.display()

if __name__ == '__main__':
    main()