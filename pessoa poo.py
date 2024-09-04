
class Pessoa:
    def __init__(self,nome: str,sexo: str,corOlhos: str,pai,mãe) -> None:
        self.__nome: str = nome
        self.__sexo: str = sexo.capitalize()
        self.__corOlhos: str = corOlhos.capitalize()
        self.__pai = pai
        self.__mãe = mãe

    # - - - - - - SET - - - - - - #

    def setSexo(self,sexo: str) -> None:
        if sexo.capitalize() == 'F':
            self.__sexo = sexo.capitalize()

    def setCorOlhos(self,corOlhos: str) -> None:
        if corOlhos.capitalize() in ['C','V','A']:
            self.__corOlhos = corOlhos.capitalize()

    # - - - - - - GET - - - - - - #

    def getSexoStr(self) -> str:
        return self.__sexo
    
    def getNomeStr(self) -> str:
        return self.__nome

    def getCorOlhosStr(self) -> str:
        return self.__corOlhos

    # - - - - - - FUN - - - - - - #

    def geraPessoa(self,nome: str, sexo: str, pai) -> None:
        if sexo.capitalize() == 'F' and pai.getSexoStr() == 'M':
            return Pessoa(nome,sexo,self.getCorOlhosStr(),pai,self.getNomeStr())
        print('ERRO')
        return None    

    def imprimeDados(self) -> None:
        print('Nome:',self.getNomeStr())
        print('Sexo:',self.getSexoStr())
        print('Cor dos olhos:',self.getCorOlhosStr())

if __name__ == '__main__':
    fulano = Pessoa('Fulano','M','A','PAI','MÃE')
    fulana = Pessoa('Fulana','F','C','PAI2','MÃE2')
    
    fulaninha = fulana.geraPessoa('Fulaninha','F',fulano)
    fulaninha.imprimeDados()
