class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self,botao):
        if botao == "+":
            print("Aumentar canal")
        elif botao == "-":
            print("Diminuir canal")
controle_remoto=ControleRemoto("preto", "10","2","2")
controle_remoto.passar_canal("+")

controle_remoto2=ControleRemoto("azul", "10","2","2")

#print(controle_remoto.cor)
#print(controle_remoto2.cor)
