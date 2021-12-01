# exemplo clientes netflix

class Cliente:

    def __init__(self, nome, email, plano):
        self.nome = nome
        self.planos = ["basic", "premium"]
        self.email = email
        if plano in self.planos:
            self.plano = plano
        else:
            print("plano inválido")

    def mudar_plano(self,novo_plano):
        if novo_plano in self.planos:
            self.plano=novo_plano
        else:
            print("plano inválido")

cliente = Cliente("Bart", "bart@gato.com", "basic")

print(cliente.plano)
cliente.mudar_plano("premium")
print("novo plano: " + cliente.plano)