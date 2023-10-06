from random import *

class Pessoa:
    def __init__(self, name: str, age: int, treinador: bool):
      self.name = name
      self.age = age
      self.treinador = treinador

class Treinador(Pessoa):
    def __init__(self, name: str, age: int):
       super().__init__(name, age, True)

class Pokemon:
    def __init__(self, nome: str, id: int, elemento: str, ataque: int, defesa: int, spataque: int, spdefesa: int, speed: int, treinador: str, vida: int):
      self.nome = nome
      self.id = id
      self.elemento = elemento
      self.ataque = ataque
      self.defesa = defesa
      self.spataque = spataque
      self.spdefesa = spdefesa
      self.speed = speed
      self.treinador = treinador
      self.vida = vida
      
    def get_treinador(self):
        print(f"O treinador de {self.nome} é {self.treinador}")

class Ataques(Pokemon):
    def __init__(self, nome: str, id: int, elemento: str, ataque: int, defesa: int, spataque: int, spdefesa: int, speed: int, treinador: str, vida: int):
       super().__init__(nome, id, elemento, ataque, defesa, spataque, spdefesa, speed, treinador, vida)
       
    def ataque_rapido(self):
        ataque_rapido_dano = self.ataque
        ataque_rapido_speed = self.speed * randint(1, 10)
        
        return ataque_rapido_dano, ataque_rapido_speed
    
    def ataque_de_folhas(self):
        ataque = "Sp_Atk"
        if (self.elemento == "Grama"):
            ataque_de_folhas_dano = self.spataque
            ataque_de_folhas_speed = self.speed * randint(1, 5)
        else:
            return "Este pokemon não pode usar este ataque."
            
        return ataque_de_folhas_dano, ataque_de_folhas_speed, ataque
    
    def bola_eletrica(self):
        ataque = "Sp_Atk"
        if (self.elemento == "Elétrico"):
            bola_eletrica_dano = self.spataque * randint(0, 3)
            bola_eletrica_speed = self.speed * randint(1, 10)
        else: 
            return "Este pokemon não pode usar este ataque"

        return bola_eletrica_dano, bola_eletrica_speed, ataque
    
    def atacar(self, ataque0: any, ataque1: any, pokemon: Pokemon):
        ataque0_dano = ataque0[0]
        ataque1_dano = ataque1[0]
        
        if (ataque0[1] > ataque1[1]):
            # print(self.nome)
            
            if (ataque0[2] == "Sp_Atk"):
                pokemon.vida = ataque_sp_atk(pokemon.vida, ataque0_dano, pokemon.spdefesa)
            else:
                pokemon.vida = ataque_f_atk(pokemon.vida, ataque0_dano, pokemon.defesa)
                
            vida_atual(pokemon.nome, pokemon.vida)
            
            if (ataque1[2] == "Sp_Atk"):
                self.vida = ataque_sp_atk(self.vida, ataque0_dano, self.spdefesa)
            else:
                self.vida = ataque_f_atk(self.vida, ataque0_dano, self.defesa)
                
            vida_atual(self.nome, self.vida)
        else:
            # print(pokemon.nome)
            
            if (ataque1[2] == "Sp_Atk"):
                self.vida = ataque_sp_atk(self.vida, ataque0_dano, self.spdefesa)
            else:
                self.vida = ataque_f_atk(self.vida, ataque0_dano, self.defesa)
                
            vida_atual(self.nome, self.vida)
            
            if (ataque0[2] == "Sp_Atk"):
                pokemon.vida = ataque_sp_atk(pokemon.vida, ataque0_dano, pokemon.spdefesa)
            else:
                pokemon.vida = ataque_f_atk(pokemon.vida, ataque0_dano, pokemon.defesa)
                
            vida_atual(pokemon.nome, pokemon.vida)

def ataque_sp_atk(vida: int, dano: int, defesa: int):
        vida_final = vida - (dano / defesa)
        
        return vida_final
    
def ataque_f_atk(vida: int, dano: int, defesa: int):
    vida_final = vida - (dano / defesa)
        
    return vida_final

def vida_atual(nome: str, vida: int):
    print(f"{nome} ficou com {vida}")
        
pikachu = Ataques("Pikachu", 4, "Elétrico", 10, 10, 20, 20, 30, "Ash", 40)

pikachu.get_treinador()

bulbassaur = Ataques("Bulbassaur", 1, "Grama", 5, 20, 25, 10, 20, "Red", 50)

bulbassaur.get_treinador()

pikachu.atacar(pikachu.bola_eletrica(), bulbassaur.ataque_de_folhas(), bulbassaur)
