import math     # módulo
print('Bienvenido al programa de áreas')
r = float(input('Ingresa un radio >= 0: '))
if r < 0:
    print('Favor ingrese un radio >= 0')
else:
    print('El área es:', math.round(math.pi*r**2, 4))

