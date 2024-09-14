from robo import Robo
import random

class RoboMedico(Robo):
    def __init__(self, nome: str, vida: float):
        super().__init__(nome, vida)
        self._poder_de_cura = random.uniform(0, 1) 
    
    @property
    def poder_de_cura(self):
        return self._poder_de_cura

    def curar(self, outro_robo):
        """Cura outro robô se a vida dele estiver abaixo de 1"""
        if outro_robo.vida < 1:
            cura_aplicada = min(1 - outro_robo.vida, self._poder_de_cura)
            outro_robo.vida += cura_aplicada
            print(f"{self.nome} curou {outro_robo.nome} em {cura_aplicada:.2f} pontos de vida.")
        else:
            print(f"{outro_robo.nome} já está com a vida cheia e não precisa de cura.")
    
if __name__ == "__main__":
    robo_medico = RoboMedico("Medico1", 0.9)
    robo1 = Robo("Delta", 0.3)
    
    print(robo_medico)
    print(robo1)
    
    robo_medico.curar(robo1)
    print(robo1)
