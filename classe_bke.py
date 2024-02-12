class Bike:
    def __init__(self, cor, modelo, ano, valor):
        print('Inicializando a classe...')
        self.cor = cor 
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor 

    # def __str__(self) -> str:
        # return f'{self.__class__.__name__}: cor: {self.cor}, modelo: {self.modelo}, ano: {self.ano}, valor: R$ {self.valor:.2f}'

    def __str__(self):
        return f"{self.__class__.__name__} {' '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

    def buzinar(self):
        print('Plim Plim!')
    
    def parar(self):
        print('Freiando!!!')
    
    def correr(self):
        print('Correndo!!!')
    
    def __del__(self):
        print('Destruindo a instância...')

bike1 = Bike('vermelha', 'masculino', 2019, 1500)

Bike.buzinar(bike1)
print(bike1)


