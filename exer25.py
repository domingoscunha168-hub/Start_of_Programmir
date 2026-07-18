class Fretes_e_transportes:
    def __init__(self, distancia, peso, tipo_de_frete):
        self.distancia = distancia
        self.peso = peso
        self.tipo_de_frete = tipo_de_frete

    def calcular_custo(self):
        if self.tipo_de_frete == "normal":
            custo_por_km = 1.5
        elif self.tipo_de_frete == "expresso":
            custo_por_km = 2.5
        else:
            raise ValueError("Tipo de frete inválido. Use 'normal' ou 'expresso'")

        custo_total = (self.distancia * custo_por_km) + (self.peso * 0.5)
        return f'Custo total: R$ {custo_total:.2f}'

frete1 = Fretes_e_transportes(100, 50, "normal")

print(frete1.calcular_custo())
frete2 = Fretes_e_transportes(200, 30, "expresso")
print(frete2.calcular_custo())
print("Cálculo de frete concluído com sucesso")