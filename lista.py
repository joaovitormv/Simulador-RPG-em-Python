#João Vitor Maximiano Vieira - 2° Informática

import random

class TipoPersonagem:
    GUERREIRO = 1
    MAGO = 2
    ARQUEIRO = 3

class Personagem:
    def __init__(self, n, t):
        self.__nome = n
        self.__tipo = t
        self.__resistencia = random.randint(10, 30)
        if self.__tipo == TipoPersonagem.GUERREIRO:
            while True:
                self.__ataque = random.randint(1, 20)
                self.__defesa = random.randint(1, 20)
                self.__magia = random.randint(1, 20)
                self.__agilidade = 28 - (self.__ataque + self.__defesa + self.__magia)
                if not (( self.__ataque + self.__magia + self.__agilidade + self.__defesa )<= 40 and max(self.__ataque, self.__magia, self.__agilidade, self.__defesa) == self.__ataque):
                    break
            
        elif self.__tipo == TipoPersonagem.MAGO:
            while True:
                self.__ataque = random.randint(1, 20)
                self.__defesa = random.randint(1, 20)
                self.__magia = random.randint(1, 20)
                self.__agilidade = 28 - (self.__ataque + self.__defesa + self.__magia)
                if not (( self.__ataque + self.__magia + self.__agilidade + self.__defesa)<= 40 and max(self.__ataque, self.__magia, self.__agilidade, self.__defesa) == self.__magia):
                    break
        elif self.__tipo == TipoPersonagem.ARQUEIRO:
            while True:
                self.__agilidade = random.randint(1, 20)
                self.__defesa = random.randint(1, 20)
                self.__magia = random.randint(1, 20)
                self.__ataque = 28 - (self.__agilidade + self.__defesa + self.__magia)
                if not (( self.__ataque + self.__magia + self.__agilidade + self.__defesa)<= 40 and max(self.__ataque, self.__magia, self.__agilidade, self.__defesa) == self.__agilidade):
                    break
    def usarAtaque(self, inimigo):
        return ( random.randint(1, 6) * self.__ataque - random.randint(1, 6) * inimigo.__defesa)
    def usarMagia(self, inimigo):
        return ( random.randint(1, 8) * self.__magia - random.randint(1, 8) * inimigo.__defesa)
    
    def get_nome(self):
        return self.__nome
    def get_tipo(self):
        return self.__tipo
    def get_resistencia(self):
        return self.__resistencia
    def get_ataque(self):
        return self.__ataque
    def get_defesa(self):
        return self.__defesa
    def get_magia(self):
        return self.__magia
    def get_agilidade(self):
        return self.__agilidade
    
    def set_nome(self, nome):
        self.__nome = nome
    def set_tipo(self, tipo):
        self.__tipo = tipo
    def set_resistencia(self, resistencia):
        self.__resistencia = resistencia
    def set_ataque(self, ataque):
        self.__ataque = ataque
    def set_defesa(self, defesa):
        self.__defesa = defesa
    def set_magia(self, magia):
        self.__magia = magia
    def set_agilidade(self, agilidade):
        self.__agilidade = agilidade

n = input("Informe o nome do personagem 1: ")
t = 0
while(t != 1 and t != 2 and t != 3):
    t = int(input(f"Informe o tipo de {n}: \n1 - Guerreiro\n2 - Mago\n3 - Arqueiro\n"))
p1 = Personagem(n, t)
n = input("Informe o nome do personagem 2: ")
t = 0
while(t != 1 and t != 2 and t != 3):
    t = int(input(f"Informe o tipo de {n}: \n1 - Guerreiro\n2 - Mago\n3 - Arqueiro\n"))
p2 = Personagem(n, t)

turno = 0
ganhou = False
while(turno <= 10 or ganhou == False ):
    turno = turno + 1
    print("Turno 1: \n")
    if p1.get_agilidade() > p2.get_agilidade():
        if(p1.get_ataque() > p1.get_magia()):
            dano = p1.usarAtaque(p2)
            if dano > p2.get_resistencia():
                ganhou = True
                print(f"{p1.get_nome()} atacou {p2.get_nome()} e deu um dano de {dano}")
                print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}")
                print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
                print(f"{p1.get_nome()} venceu.\n")
            else:
                print(f"{p1.get_nome()} atacou {p2.get_nome()} e deu um dano de {dano}\n")
                print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
        else:
            dano = p1.usarMagia(p2)
            if dano > p2.get_resistencia():
                ganhou = True
                print(f"{p1.get_nome()} soltou uma magia em {p2.get_nome()} e deu um dano de {dano}\n")
                print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
                print(f"{p1.get_nome()} venceu.\n")
            else:
                print(f"{p1.get_nome()} atacou {p2.get_nome()} e deu um dano de {dano}\n")
                print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")

    elif p1.get_agilidade() < p2.get_agilidade():
        if(p2.get_ataque() > p2.get_magia()):
            dano = p2.usarAtaque(p1)
            if dano > p1.get_resistencia():
                ganhou = True
                print(f"{p2.get_nome()} atacou {p1.get_nome()} e deu um dano de {dano}\n")
                print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
                print(f"{p2.get_nome()} venceu.\n")
            else:
                print(f"{p2.get_nome()} atacou {p1.get_nome()} e deu um dano de {dano}\n")
                print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
        else:
            dano = p2.usarMagia(p1)
            if dano > p1.get_resistencia():
                ganhou = True
                print(f"{p2.get_nome()} soltou uma magia em {p1.get_nome()} e deu um dano de {dano}\n")
                print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
                print(f"{p2.get_nome()} venceu.\n")
            else:
                print(f"{p2.get_nome()} atacou {p1.get_nome()} e deu um dano de {dano}\n")
                print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
    else: #3 opção
        x = random.randint(1, 2)
        if x == 1:
            if(p1.get_ataque() > p1.get_magia()):
                dano = p1.usarAtaque(p2)
                if dano > p2.get_resistencia():
                    ganhou = True
                    print(f"{p1.get_nome()} atacou {p2.get_nome()} e deu um dano de {dano}")
                    print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}")
                    print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                    print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                    print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                    print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                    print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                    print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                    print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                    print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                    print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
                    print(f"{p1.get_nome()} venceu.\n")
                else:
                    print(f"{p1.get_nome()} atacou {p2.get_nome()} e deu um dano de {dano}\n")
                    print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                    print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                    print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                    print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                    print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                    print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                    print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                    print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                    print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                    print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
            else:
                dano = p1.usarMagia(p2)
                if dano > p2.get_resistencia():
                    ganhou = True
                    print(f"{p1.get_nome()} soltou uma magia em {p2.get_nome()} e deu um dano de {dano}\n")
                    print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                    print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                    print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                    print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                    print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                    print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                    print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                    print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                    print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                    print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
                    print(f"{p1.get_nome()} venceu.\n")
                else:
                    print(f"{p1.get_nome()} atacou {p2.get_nome()} e deu um dano de {dano}\n")
                    print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                    print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                    print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                    print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                    print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                    print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                    print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                    print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                    print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                    print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
        else: #3.2 opção
            if(p2.get_ataque() > p2.get_magia()):
                dano = p2.usarAtaque(p1)
                if dano > p1.get_resistencia():
                    ganhou = True
                    print(f"{p2.get_nome()} atacou {p1.get_nome()} e deu um dano de {dano}\n")
                    print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                    print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                    print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                    print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                    print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                    print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                    print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                    print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                    print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                    print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
                    print(f"{p2.get_nome()} venceu.\n")
                else:
                    print(f"{p2.get_nome()} atacou {p1.get_nome()} e deu um dano de {dano}\n")
                    print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                    print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                    print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                    print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                    print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                    print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                    print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                    print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                    print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                    print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
            else:
                dano = p2.usarMagia(p1)
            if dano > p1.get_resistencia():
                ganhou = True
                print(f"{p2.get_nome()} soltou uma magia em {p1.get_nome()} e deu um dano de {dano}\n")
                print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
                print(f"{p2.get_nome()} venceu.\n")
            else:
                print(f"{p2.get_nome()} atacou {p1.get_nome()} e deu um dano de {dano}\n")
                print(f"A resistência de {p2.get_nome()} é de {p2.get_resistencia()}\n")
                print(f"A defesa de {p2.get_nome()} é de {p2.get_defesa()}")
                print(f"A agilidade de {p2.get_nome()} é de {p2.get_agilidade()}")
                print(f"A magia de {p2.get_nome()} é de {p2.get_magia()}")
                print(f"O ataque de {p2.get_nome()} é de {p2.get_ataque()}\n\n")
                print(f"A resistência de {p1.get_nome()} é de {p1.get_resistencia()}")
                print(f"A defesa de {p1.get_nome()} é de {p1.get_defesa()}")
                print(f"A agilidade de {p1.get_nome()} é de {p1.get_agilidade()}")
                print(f"A magia de {p1.get_nome()} é de {p1.get_magia()}")
                print(f"O ataque de {p1.get_nome()} é de {p1.get_ataque()}\n\n\n\n")
            
        