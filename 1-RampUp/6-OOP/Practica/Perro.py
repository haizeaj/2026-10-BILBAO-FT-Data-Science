class Perro:
    '''
     los atributos que todos los perros tienen
    '''
    patas = 4 
    orejas = 2
    ojos = 2
    
    def __init__(self, raza, pelo="Marron", dueño=False):
        '''atributos para identificar al perro
        '''
        self.raza = raza
        self.pelo = pelo
        self.dueño = dueño
        self.velocidad = 0

    def andar(self, aumento_velocidad):
        '''velocidad del perro
        '''
        self.velocidad = self.velocidad + aumento_velocidad
        return self.velocidad 
    
    def parar(self):
        '''lograr que el perro se pare
        '''
        self.velocidad = 0
        return self.velocidad

    def ladrar(self, ladrido):
        '''Escribir lo que quiere significar el ladrido
        '''
        return "Guau " + ladrido