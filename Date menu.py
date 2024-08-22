import os



class Data:

    def __init__(self, dia, mês, ano):
        
        self.mês = int(mês)
        self.dia = int(dia)
        self.ano = int(ano)
        
        
    def displayData(self):

        if self.mês > 10:
            print(f'{self.dia} / {self.mês} / {self.ano}')
        else:
            print(f'{self.dia} / 0{self.mês} / {self.ano}')

    
        return
    def changeData(self):
        self.dia = int(input('Digite o dia: '))
        self.mês = int(input('Digite o mês: '))
        self.ano = int(input('Digite o ano: '))
    def birthday(self):
        ba = int(input('Digite o ano do seu aniversário: '))
        print(f'Você tem {self.ano - ba} anos')

if __name__ == '__main__':
    data = Data(0,0,0)
    
    while True:
        
        op = int(input('\tMenu\n1 - Mudar a data.\n2 - Ver a data atual;\n3 - Idade;\n0 - Sair.\nSelecionar: '))
        os.system('cls')
        if op == 1:
            data.changeData()
            os.system('cls')
        elif op == 2:
            data.displayData()
            input()
            os.system('cls')
        elif op == 3:
            data.birthday()
            input()
            os.system('cls')
        elif op == 0:
            os.system('cls')
            print('Programa encerrado.')
            break
        else:
            input('Não entendi, digite novamente.')
            os.system('cls')
            
    
