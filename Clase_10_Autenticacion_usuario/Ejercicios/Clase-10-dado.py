import random

suma = 0 
while suma !=12:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma = dado1 + dado2
    
    print(f"Lanzaste {dado1} y {dado2}. La suma es: {suma}")
    