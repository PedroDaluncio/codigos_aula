from ave import Ave


class Canarinho(Ave):
    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo, altura_voo)

    def cantar(self):
        super().produzir_som()
        return "AVE: PRODUZ SOM: PIU"
