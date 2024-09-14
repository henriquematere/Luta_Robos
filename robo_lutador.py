from robo import Robo
import random

class RoboLutador(Robo):
    dano_maximo = 0.4  

    def __init__(self, nome: str, vida: float):
        super().__init__(nome, vida)
        self._poder_de_luta = random.uniform(RoboLutador.dano_maximo, 1)  
    
    @property
    def poder_de_luta(self):
        return self._poder_de_luta

    def atacar(self, outro_robo):
        """Ataca outro robô, reduzindo sua vida de acordo com o poder de luta."""
        if outro_robo.vida > 0:
            dano = outro_robo.vida * (1 - self._poder_de_luta)
            outro_robo.vida -= dano
            print(f"{self.nome} atacou {outro_robo.nome} e causou {dano:.2f} de dano!")
            
            if isinstance(outro_robo, RoboLutador):
                outro_robo.contra_atacar(self)
        else:
            print(f"{outro_robo.nome} já está fora de combate!")

    def contra_atacar(self, atacante):
        """Contra-ataca o robô atacante"""
        if self.vida > 0:
            dano = atacante.vida * (1 - self._poder_de_luta)
            atacante.vida -= dano
            print(f"{self.nome} contra-atacou {atacante.nome} e causou {dano:.2f} de dano!")
        else:
            print(f"{self.nome} não pode contra-atacar porque já foi derrotado.")

if __name__ == "__main__":
    lutador1 = RoboLutador("Lutador1", 0.8)
    lutador2 = RoboLutador("Lutador2", 0.7)
    
    print(lutador1)
    print(lutador2)
    
    lutador1.atacar(lutador2)
    print(lutador2)
