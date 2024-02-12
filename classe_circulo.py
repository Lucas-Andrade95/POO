class Círculo:
    def __init__(self, raio):
        self.raio = raio

    
    def area(self):
        area = 3.14 * (self.raio**2)
        return area
    
    def perimetro(self):
        perimetro = 2 * 3.14 * self.raio
        return perimetro
        
    
circulo1 = Círculo(float(input('Raio do círculo (m): ')))
area = circulo1.area()
perimetro = circulo1.perimetro()
print(f'O círculo tem {area}m² de área e {perimetro:.2f}m de perímetro')
