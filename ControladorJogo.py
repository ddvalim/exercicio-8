from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagems = []

    @property
    def baralho(self) -> list:
        return self.__baralho
    @property
    def personagems(self) -> list:
        return self.__personagems

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        p = Personagem(energia, habilidade, velocidade, resistencia, tipo)
        self.__personagems.append(p)
        return p

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        c = Carta(personagem)
        self.__baralho.append(c)
        return c

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        jogador1.mao = random.choice(self.__baralho)
        jogador2.mao = random.choice(self.__baralho)

    def jogada(self, mesa: Mesa) -> Jogador:
        c1 = mesa.carta_jogador1.valor_total_carta()
        c2 = mesa.carta_jogador2.valor_total_carta()
        
        carta1 = mesa.carta_jogador1
        carta2 = mesa.carta_jogador2
        
        if c1 > c2:
            mesa.jogador1.inclui_carta_na_mao(carta1)
            mesa.jogador1.inclui_carta_na_mao(carta2)
        
        elif c2 > c1:
            mesa.jogador2.inclui_carta_na_mao(carta1)
            mesa.jogador2.inclui_carta_na_mao(carta2)

        else:
            mesa.jogador1.inclui_carta_na_mao(carta1)
            mesa.jogador2.inclui_carta_na_mao(carta2)

        if len(mesa.jogador1.mao) == 0:
            return mesa.jogador2
        elif len(mesa.jogador2.mao) == 0:
            return mesa.jogador1
        else:
            return None
        