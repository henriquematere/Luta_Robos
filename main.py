from robo import Robo
from robo_medico import RoboMedico
from robo_lutador import RoboLutador
import random

def acionar_medico(robo_medico, robo_ferido):
    if random.random() > 0.5:
        robo_medico.curar(robo_ferido)
    else:
        print(f"{robo_medico.nome} não atendeu ao chamado para curar {robo_ferido.nome}.")

if __name__ == "__main__":
    lutador1 = RoboLutador("Lutador1", 0.8)
    lutador2 = RoboLutador("Lutador2", 0.7)
    medico1 = RoboMedico("Medico1", 0.9)
    
    robos_lutadores = [lutador1, lutador2]
    robos_medicos = [medico1]
    
    rodada = 1
    max_rodadas = 10
    while any(robo.vida > 0 for robo in robos_lutadores) and rodada <= max_rodadas:
        print(f"\n--- Rodada {rodada} ---")
        
        if lutador1.vida > 0:
            lutador1.atacar(lutador2)
        
        if lutador2.vida <= 0:
            print(f"{lutador2.nome} foi derrotado! {lutador1.nome} venceu a luta!")
            break

        if lutador2.vida < 0.1 and lutador2.vida > 0:
            acionar_medico(medico1, lutador2)
        
        if lutador2.vida > 0:
            lutador2.atacar(lutador1)

        if lutador1.vida <= 0:
            print(f"{lutador1.nome} foi derrotado! {lutador2.nome} venceu a luta!")
            break

        if lutador1.vida < 0.1 and lutador1.vida > 0:
            acionar_medico(medico1, lutador1)

        print(lutador1)
        print(lutador2)
        
        rodada += 1
    
    if rodada > max_rodadas:
        print("A luta terminou em um empate após atingir o limite de rodadas.")
