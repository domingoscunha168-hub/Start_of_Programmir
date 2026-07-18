class criptografia_de_senhas:
    
    def __init__(self, senha):
        self.senha = senha

    def criptografar(self):
        senha_criptografada = ""
        for char in self.senha:
            senha_criptografada += chr(ord(char) + 3)
        return senha_criptografada

    def descriptografar(self, senha_criptografada):
        senha_descriptografada = ""
        for char in senha_criptografada:
            senha_descriptografada += chr(ord(char) - 3)
        return senha_descriptografada
   
    