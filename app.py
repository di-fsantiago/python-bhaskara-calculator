import math
import cmath

while True:
    
    print("------\n")
    
    a = float(input('Insira o número a: '))
    
    if a == 0:
        print("O número de a foi informado incorretamente.")
        continue
    
    b = float(input('Insira o número b: '))
    c = float(input('Insira o número c: '))
    
    # Faz o cálculo
    delta = pow(b,2) - 4 * a * c
    
    # Se delta = 0, mostra o valor apenas 1 vez
    if delta == 0:
        x = (-b) / (2 * a)
        print(f"O valor de x é: {x}")
    
    else:
        # Se delta > 0, faz o cálculo com x' e x"
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            
        # Se não, faz o cálculo com númerio imaginário.
        else:
            x1 = (-b + cmath.sqrt(delta)) / (2 * a)
            x2 = (-b - cmath.sqrt(delta)) / (2 * a)
            
            
        print(f"O valor de x\' é = {x1}")
        print(f"O valor de x\" é = {x2}")
    print("")
