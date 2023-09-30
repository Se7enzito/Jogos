class Personagem:
    def __init__(self, name: str, vida: float, dano: float):
      self.name = name
      self.vida = vida
      self.dano = dano
      
    def atacar(self, alguem: any) -> None:
        print(f"{self.name} ataca {alguem.name}")
        
        alguem.vida = alguem.vida - self.dano
        
        print(f"Vida de {self.name} = {self.vida}")
        print(f"Vida de {alguem.name} = {alguem.vida}")
        
        input("Contra-Ataque...")
        
        print(f"{alguem.name} ataca {self.name}")
        
        self.vida = self.vida - alguem.dano
        
        print(f"Vida de {self.name} = {self.vida}")
        print(f"Vida de {alguem.name} = {alguem.vida}")
      
class Heroi(Personagem):
    def __init__(self, name: str, vida: float, dano: float, classe: str):
       super().__init__(name, vida, dano)
       self.classe = classe
    
class Mob(Personagem):
    def __init__(self, name: str, vida: float, dano: float, drop: bool):
       super().__init__(name, vida, dano)
       self.drop = drop

heroi1 = Heroi("Henrique", 100.0, 1.0, "Bardo")
heroi2 = Heroi("Lucas Baeta", 100.0, 1.2, "Elfo Noturno")

heroi1.atacar(heroi2)