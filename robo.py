import random

class Robo:
    def __init__(self, nome: str, vida: float, nivel_critico: float = 0.6):
        self._nome = nome
        self._vida = vida
        self._nivel_critico = nivel_critico
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        if len(novo_nome) > 1:
            self._nome = novo_nome
        else:
            raise ValueError("Nome deve ter mais de 1 caractere.")
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nova_vida: float):
        if 0 <= nova_vida <= 1:
            self._vida = nova_vida
        else:
            raise ValueError("A vida deve estar entre 0 e 1.")
    
    def __repr__(self):
        return f"Robo(nome={self._nome}, vida={self._vida:.2f})"
    
    def __add__(self, outro_robo):
        """Reprodução entre robôs"""
        nome_pai = self._nome.split('-')[0]
        nome_mae = outro_robo.nome.split('-')[0]
        nome_bebe = f"{nome_pai}-{nome_mae}"
        return Robo(nome_bebe, random.uniform(0, 1))

    def precisa_de_medico(self):
        """Verifica se o robô precisa de médico"""
        return self._vida < self._nivel_critico

    def ganhar_vida(self):
        """Robô ganha vida aleatória entre 0 e 1"""
        self._vida = random.uniform(0, 1)

if __name__ == "__main__":
    robo1 = Robo("Alpha", 0.5)
    robo2 = Robo("Beta", 0.4)
    
    print(robo1)
    print(robo2)

    bebe_robo = robo1 + robo2
    print(f"Filho dos robôs: {bebe_robo}")
