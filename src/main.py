class Hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "atacou"

        mensagem = f"o {self.tipo} atacou usando {ataque}"
        print(mensagem)

heroi1 = Hero("Gandalf", 1000, "mago")
heroi2 = Hero("Aragorn", 35, "guerreiro")
heroi3 = Hero("Bruce Lee", 40, "monge")
heroi4 = Hero("Hanzo", 28, "ninja")

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
