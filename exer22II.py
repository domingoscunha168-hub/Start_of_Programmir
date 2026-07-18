class Controle_Remoto:
    canal_minimo: int = 23
    canal_maximo: int = 32
    volume_minimo: int = 2
    volume_maximo: int = 3
    def __init__(self, canal: int = 23, volume: int = 2):
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False
    
    def conteudo(self):
        print(f'Canal atual: {self.canal_atual}')
        print(f'Volume atual: {self.volume_atual}')
        
    def aumentar_volume(self):
        if self.volume_atual < self.volume_maximo:
            self.volume_atual += 1
            print(f'Volume aumentado para {self.volume_atual}')
        else:
            print('Volume máximo atingido')
    def diminuir_volume(self):
        if self.volume_atual > self.volume_minimo:
            self.volume_atual -= 1
            print(f'Volume diminuído para {self.volume_atual}')
            if self.volume_atual == self.volume_minimo:
                print('Volume neutro atingido — desligando')
                self.desligar()
        else:
            print('Volume mínimo atingido')

    def aumentar_canal(self):
        if self.canal_atual < self.canal_maximo:
            self.canal_atual += 1
            print(f'Canal aumentado para {self.canal_atual}')
        else:
            print('Canal máximo atingido')
    def diminuir_canal(self):
        if self.canal_atual > self.canal_minimo:
            self.canal_atual -= 1
            print(f'Canal diminuído para {self.canal_atual}')
        else:
            print('Canal mínimo atingido') 
        
    def ligar(self):
        self.ligado = True
        print('Controle ligado')
  

    def desligar(self):
        self.ligado = False
        print('Controle desligado')
