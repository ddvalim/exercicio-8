from AbstractCarta import *
from Personagem import *

class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem = personagem
        self.__valor_total_carta = 0
    
    
    def valor_total_carta(self) -> int:
        self.__valor_total_carta = (self.__personagem.resistencia + self.__personagem.velocidade + self.__personagem.habilidade + self.__personagem.energia)
        return self.__valor_total_carta ##'int' object is not callable  faltava retornar o resultado
        
    @property
    def personagem(self) -> Personagem:
        return self.__personagem
