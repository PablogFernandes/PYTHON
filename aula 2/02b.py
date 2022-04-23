class balde:
    """animal da selva"""

    def __init__(self):

        # atributos simples
        self.marca = ""
        self.durabilidade_em_anos = 0
        self.volume = ""
        self.material = ""

    def __str__(self):
        return self.marca

        #     def __repr__(self):
        #         return self.marca

        # instanciamento

        castelo_1 = balde()
        castelo_2 = balde()

        print(castelo_1)
        print(castelo_2)
