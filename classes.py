class Pessoa:
    def __init__(self, nome, idade, vida=False):
        self.nome = nome
        self.idade = idade
        self.vida = False

    def saudacao(self):
        print(f'Olá! meu nome é {self.nome} e tenho {self.idade} anos.')
    
    def vivo(self):
        self.vida = True
        print(f'{self.nome} está vivo! ')

    def morto(self):
        self.vida = False
        print(f'{self.nome} está morto.')

pessoas = list()

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    NovaPessoa = Pessoa(nome, idade)
    pessoas.append(NovaPessoa)
    fim = input('Deseja cadastrar outra pessoa? [S/N]: ').strip().upper()
    if fim not in 'SN':
        fim = input('Sim ou Não? [S/N]: ')
    if fim == 'N':
        break

for cadaum in pessoas:
    cadaum.saudacao()
    cadaum.vivo()