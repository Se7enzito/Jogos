class Bloco():
    def __init__(self, locx: float, locy: float, locz: float, tipo: str, id: float, world: str, drop: str) -> None:
      self.locx = locx
      self.locy = locy
      self.locz = locz
      self.tipo = tipo
      self.id = id
      self.world = world
      self.location = locx, locy, locz
      self.drop = drop
      
    def set_new_location(self, loc: list):
        self.location = loc
        
    def set_new_locationx(self, locx: float):
        self.location = locx, self.location[1], self.location[2]
        self.locx = locx
        
    def set_new_locationy(self, locy: float):
        self.location = self.location[0], locy, self.location[2]
        self.locy = locy
        
    def set_new_locationz(self, locz: float):
        self.location = self.location[0], self.location[1], locz
        self.locz = locz
        
    def get_full_location(self):
        return self.location
    
    def get_locationx(self):
        return self.locx
    
    def get_locationy(self):
        return self.locy
    
    def get_locationz(self):
        return self.locz
    
    def set_new_type(self, new_tipo: str):
        self.tipo = new_tipo
        
    def get_tipo(self):
        return self.tipo
    
    def set_new_id(self, new_id: int):
        self.id = new_id
        
    def get_id(self):
        return self.id
    
    def set_new_world(self, world: str):
        self.world = world
        
    def get_world(self):
        return self.world
    
    def set_new_drop(self, drop: str):
        self.drop = drop
        
    def get_drop(self):
        return self.drop
    
    def quebrar(self):
        print(f"Quebrando o bloco {self.tipo}")
        
        print(f"O drop foi: {self.drop}")
        
    def colocar(self, locx: float, locy: float, locz: float):
        print(f"O bloco {self.tipo}, foi colocado nas coordenadas x: {locx} y: {locy} z: {locz}")
    
class Grama(Bloco):
    def __init__(self, locx: float, locy: float, locz: float, tipo: str, id: float, world: str, drop: str) -> None:
        super().__init__(locx, locy, locz, tipo, id, world, drop)
        
class Pedra(Bloco):
    def __init__(self, locx: float, locy: float, locz: float, tipo: str, id: float, world: str, drop: str) -> None:
        super().__init__(locx, locy, locz, tipo, id, world, drop)
        
grama_seca = Grama(1.0, 1.0, 1.0, "Grama Seca", 1, "Normal", "Grama Seca")
pedregulho = Pedra(1.0, 2.0, 3.0, "Pedregulho", 1, "Normal", "Pedregulho")

grama_seca.quebrar()
grama_seca.colocar()

pedregulho.quebrar()
pedregulho.colocar()