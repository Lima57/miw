from abc import ABC, abstractmethod


# usuários:

# coordenador
# colaborador
# colab lider
# colab membro
# colab tercerizado
# participante


class Usuario(ABC):

    def __init__(self, nome, senha, id, ocu):
        self._nome = nome
        self.__senha = senha
        self._identificacao = id
        self._ocupacao = ocu

    @property
    def nome(self):
        return self._nome

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
            self._nome = nome
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
        return f'{self._nome.title}, {self.__senha}, {self._identificacao.title}, {self._ocupacao.title}'

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


class Admin(Usuario):

    def __init__(self, nome, senha, id, ocu, setor):
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


class Visitante(Usuario):

    def __init__(self, nome, senha, id, ocu):
        super().__init__(nome, senha, id, ocu)


class Colaborador(Usuario):

    def __init__(self, nome, senha, id, ocu, setor, eq):
        super().__init__(nome, senha, id, ocu)
        self.setor = setor
        self.equipe = eq

    def getColaborador(self):
        return f'{self.setor.title}, {self.equipe.title}'


class ColabLider(Colaborador):

    def __init__(self, nome, senha, id, ocu, setor, eq):
        super().__init__(nome, senha, id, ocu, setor, eq)


class ColabMembro(Colaborador):

    def __init__(self, nome, senha, id, ocu, setor, eq):
        super().__init__(nome, senha, id, ocu, setor, eq)


class ColabTercerizado(Colaborador):

    def __init__(self, nome, senha, id, ocu, setor, eq):
        super().__init__(nome, senha, id, ocu, setor, eq)
