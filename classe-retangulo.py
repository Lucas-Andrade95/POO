class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)

retangulos = []
cont = 1
print('--- CÁLCULO DE ÁREA E PERÍMETRO DO RETÂNGULO ---')
while True:
    print(f'RETÂNGULO {cont}')
    ret_base = float(input('Base do Retângulo: '))
    ret_altura = float(input('Altura do Retângulo: '))
    retangulo = Retangulo(ret_base, ret_altura)
    retangulos.append(retangulo)
    cont += 1
    fim = input('Deseja cadastrar outro retângulo? [S/N]: ').upper().strip()
    if fim not in 'SN':
        fim = input('Sim ou não? [S/N]').upper().strip()
    if fim == 'N':
        break

print('~'*50)
for i, retangulo in enumerate(retangulos, start=1):
    area = retangulo.area()
    perimetro = retangulo.perimetro()
    print(f'A área do retângulo {i} é {area}m² e o perímetro é {perimetro}m.')
