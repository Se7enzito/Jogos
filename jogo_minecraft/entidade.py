class Entidade():
    def __init__(self, name: str, age: int, height: float, strenght: int, tipo: str, dano: float, vida: float):
      self.name = name
      self.age = age
      self.height = height
      self.strenght = strenght
      self.tipo = tipo
      self.dano = dano
      self.vida = vida
      
    def set_new_name(self, name: str):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_new_age(self, age: int):
        self.age = age
        
    def get_age(self):
        return self.age
    
    def set_new_height(self, height: int):
        self.height = height
        
    def get_height(self):
        return self.height
    
    def set_new_strenght(self, strenght: int):
        self.strenght = strenght
        
    def get_strenght(self):
        return self.strenght
    
    def set_new_tipo(self, tipo: str):
        self.tipo = tipo
    
    def get_tipo(self):
        return self.tipo
    
    def set_new_vida(self, vida: float):
        self.vida = vida
    
    def get_vida(self):
        return self.vida
    
    def set_new_dano(self, dano: float):
        self.dano = dano
        
    def get_dano(self):
        return self.dano
    
    def atacar(self, alguem: any):
        print(f"{self.name} ataca {alguem.name}")
        
        alguem.vida = alguem.vida - self.dano
        
        print(f"Vida de {self.name} = {self.vida}")
        print(f"Vida de {alguem.name} = {alguem.vida}")
        
        input("Contra-Ataque...")
        
        print(f"{alguem.name} ataca {self.name}")
        
        self.vida = self.vida - alguem.dano
        
        print(f"Vida de {self.name} = {self.vida}")
        print(f"Vida de {alguem.name} = {alguem.vida}")
        
    def curar(self, cura: float):
        print(f"{self.name}: Vida atual {self.vida}")
        
        self.vida = cura + self.vida
        
        print(f"{self.name}: Sua nova vida {self.vida}")
    
class Player(Entidade):
    def __init__(self, name: str, age: int, strenght: int, dano: float, vida: float):
      super().__init__(name, age, 2.0, strenght, "Normal", dano, vida)
      
class Mob(Entidade):
    def __init__(self, name: str, age: int, height: float, strenght: int, tipo: str, dano: float, vida: float):
        super().__init__(name, age, height, strenght, tipo, dano, vida)
        
p1 = Player("Bernardo", 10, 10, 10.0, 100.0)
p2 = Player("Higor", 10, 10, 5.0, 200.0)

p1.atacar(p2)
p2.curar(5.0)