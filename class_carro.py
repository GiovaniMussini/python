class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor



class Motor:
    def __init__(self, nome) -> None:
        self.nome = nome
    
class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome


carro = Carro('296 GTB')
fabricante = Fabricante('Ferrari')
motor = Motor('3.0 L V6 Electric')
carro.fabricante = fabricante
carro.motor = motor

print('Carro:', carro.nome)
print('Fabricante:', carro.fabricante.nome)
print('Motor:', carro.motor.nome)

carro = Carro('X1')
fabricante = Fabricante('BMW')
motor = Motor('1.5 turbo de 156 cv e 24,5 kgfm')
carro.fabricante = fabricante
carro.motor = motor
print()
print('Carro:', carro.nome)
print('Fabricante:', carro.fabricante.nome)
print('Motor:', carro.motor.nome)
