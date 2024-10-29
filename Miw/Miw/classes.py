from abc import ABC, abstractmethod


# usuários:

# coordenador
# colaborador
# colab lider
# colab membro
# colab tercerizado
# participante


class Usuario(ABC):

    def __init__(self, nome : str, senha : str , id : str, ocu : str, visitante : bool , colaborador : bool):
        self.__nome = nome
        self.__senha = senha
        self._identificacao = id
        self._ocupacao = ocu
        self.visitante = visitante
        self.colaborador = colaborador

    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha

    @property
    def identificacao(self):
        return self._identificacao

    @property
    def ocupacao(self):
        return self._ocupacao

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("O nome deve ser uma string.")

    @senha.setter
    def senha(self, senha):
        if len(senha) >= 8:
            self.__senha = senha
        else:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")

    @identificacao.setter
    def identificacao(self, identificacao):
        self._identificacao = identificacao

    @ocupacao.setter
    def ocupacao(self, ocupacao):
        self._ocupacao = ocupacao

    def getUsuario(self):
        return f'{self.__nome.title}, {self.__senha}, {self._identificacao.title}, {self._ocupacao.title}'

    def Collect(self, num):
        if num == '1' or 'VISITANTE' in num.upper():
            nome = input("Digite seu nome:")
            senha = input("Digite sua senha:")
            id = input("Digite seu id:")
            ocup = input("Digite sua ocupação:")
            return nome, senha, id, ocup
        elif num in ['2', '3', '4', '5'] or ['COLABORADOR','LÍDER','MEMBRO','TERCERIZADO'] in num.upper():
            nome = input("Digite seu nome:")
            senha = input("Digite sua senha:")
            id = input("Digite seu id:")
            ocup = input("Digite sua ocupação:")
            setor = input("Digite seu setor:")
            equipe = input("Digite sua equipe:")
            return nome, senha, id, ocup, setor, equipe
        elif num == '6' or 'ADMINISTRADOR' in num.upper():
            nome = input("Digite seu nome:")
            senha = input("Digite sua senha:")
            id = input("Digite seu id:")
            ocup = input("Digite sua ocupação:")
            setor = input("Digite seu setor:")
            return nome, senha, id, ocup, setor
        
    def InscricaoEvento():
        pass 
        # ------------------------ a desenvolver --------------------------------

class Admin(Usuario):

    def __init__(self, nome, senha, id, ocu, setor : str):
        super().__init__(nome, senha, id, ocu)
        self._setor = setor

    @property
    def setor(self):
        return self._setor
    
    @setor.setter
    def setor(self, setor):
        self._setor = setor

    def getAdmin(self):
        return f'{self.setor.title}'
    
    def gerenciarEvento():
        pass
        # ------------------------ a desenvolver --------------------------------

class Colaborador(Usuario):

    def __init__(self, nome, senha, id, ocu, setor : str, tercerizado : bool):
        super().__init__(nome, senha, id, ocu)
        self.__setor = setor
        self.__tercerizado = tercerizado
        # retirei a caracteristica equipe pois não tem no diagrama

    def getColaborador(self):
        return f'{self.__setor.title}, {self.__tercerizado.title}'

    def getsetor(self):
        return self.__setor 

class ColabLider(Colaborador):

    def __init__(self, nome, senha, id, ocu, setor, eq):
        super().__init__(nome, senha, id, ocu, setor, eq)


class ColabMembro(Colaborador):

    def __init__(self, nome, senha, id, ocu, setor, eq):
        super().__init__(nome, senha, id, ocu, setor, eq)
