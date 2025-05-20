class Atleta():
    def __init__(self, peso):
        self.aposentado = False
        self.peso = peso
        self.correndo = False
        self.nadando = False
        self.pedalando = False

    def atletaaposentado(self):
        resposta = input("o atleta é aposentado? digite 'sim' ou 'não':\n")
        if resposta.lower() == "sim":
            self.aposentado = True
            print("o atleta esta aposentado e não pode aquecer")

    def aquecer(self):
        if self.aposentado:
            print("o atleta esta aposentado e não pode aquecer")
        else:
            print("o atleta esta se aquecendo")


class Corredor(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def correr(self):
        if self.aposentado:
            print("o atleta esta aposentado e não pode correr")
        elif self.nadando or self.pedalando:
            print("o atleta esta fazendo outra atividade e não pode correr")
        else:
            self.correndo = True
            self.nadando = False
            self.pedalando = False
            print("o atleta esta correndo")


class Nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def nadar(self):
        if self.aposentado:
            print("o atleta esta aposentado e não pode nadar")
        elif self.correndo or self.pedalando:
            print("o atleta esta fazendo outra atividade e não pode nadar")
        else:
            self.correndo = False
            self.nadando = True
            self.pedalando = False
            print("o atleta esta nadando")


class Ciclista(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def pedalar(self):
        if self.aposentado:
            print("o atleta esta aposentado e não pode pedalar")
        elif self.nadando or self.correndo:
            print("o atleta esta fazendo outra atividade e não pode pedalar")
        else:
            self.correndo = False
            self.nadando = False
            self.pedalando = True
            print("o atleta esta pedalando")


class Triatleta(Corredor, Nadador, Ciclista):
    def __init__(self, peso):
        Atleta.__init__(self, peso)