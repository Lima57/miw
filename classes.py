from abc import ABC, abstractmethod


# usuários:

# coordenador
# colaborador
# colab lider
# colab membro
# colab tercerizado
# participante


# A classe Usuario represente uma superclasse, sendo herdada por demais classes. Elas serão especificadas pelo código.
class Usuario(ABC):

    def __init__(self, nome : str, senha : str , id : str, ocu : str):
        self.__nome = nome
        self.__senha = senha
        self._identificacao = id
        self._ocupacao = ocu
        self.visitante = False
        self.colaborador = False

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
        return f'{self.__nome}, {self.__senha}, {self._identificacao}, {self._ocupacao}'

    def Collect(self, num):
        if num == '1' or 'VISITANTE' in num.upper():
            nome = input("Digite seu nome:")
            senha = input("Digite sua senha:")
            id = input("Digite seu id:")
            ocup = input("Digite sua ocupação:")
            return nome, senha, id, ocup
        elif num in '2' or 'COLABORADOR' in num.upper():
            nome = input("Digite seu nome:")
            senha = input("Digite sua senha:")
            id = input("Digite seu id:")
            ocup = input("Digite sua ocupação:")
            setor = input("Digite seu setor:")
            return nome, senha, id, ocup, setor
        elif num == '3' or 'ADMINISTRADOR' in num.upper():
            nome = input("Digite seu nome:")
            senha = input("Digite sua senha:")
            id = input("Digite seu id:")
            ocup = input("Digite sua ocupação:")
            setor = input("Digite seu setor:")
            return nome, senha, id, ocup, setor
    
    def setVisitante(self):
        self.visitante = True
    def setColab(self):
        self.colaborador = True
        
    def InscricaoEvento(self,CEvento,NParticipante):
        CEvento.addParticipante(NParticipante)
    
class Competicao():
    def __init__ (self, descricao: str, limite_participantes: int):
        self.descricao = descricao
        self.limite_participantes = limite_participantes
        self.participantes = []

    def getDescricaoComp(self):
        return self.descricao

    def addParticipanteComp(self,NParticipante):
        self.participantes.append(NParticipante)

class Oficina():
    def __init__ (self, descricao: str, limite: int):
        self.descricao = descricao
        self.limite = limite
        self.participantes = []

    def getDescricaoOfic(self):
        return self.descricao

    def addParticipanteOfic(self,NParticipante):
        self.participantes.append(NParticipante)

# Os atributos "competicao" e "oficina" na classe são objetos das classes "Competicao" e "Oficina", respectivamente, agregando a "Evento".
class Evento:
    def __init__(self, titulo: str, horarioInicio: int, horarioFim: int, data: int, competicao, oficina):
        self.titulo = titulo
        self.horarioInicio = horarioInicio
        self.horarioFim = horarioFim
        self.data = data
        self.competicao = competicao
        self.oficina = oficina
        self.participantes = []
        self.local = None

    def setEvento(self, titulo: str, horarioInicio: int, horarioFim: int, data: int, competicao, oficina):
        self.titulo = titulo
        self.horarioInicio = horarioInicio
        self.horarioFim = horarioFim
        self.data = data
        self.competicao = competicao
        self.oficina = oficina

    def setLocal(self,local):
        self.local = local
        
    def addParticipante(self,NParticipante):
        self.participantes.append(NParticipante)

    def getParticipantes(self):
        for i in self.participantes: 
            return i 
        
    def getTitulo(self):
        return self.titulo
    
    def getEvento(self):
        print(f'''\nEvento: {self.titulo}
Horário de início: {self.horarioInicio}h
Horário de fim: {self.horarioFim}h
Data: {self.data}
''')
        
# Herda de Usuario
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
    
    def gerenciamentoEvento(self, evento: Evento, titulo: str, horarioInicio: int, horarioFim: int, data: int, competencia, oficina):
        evento.setEvento(titulo, horarioInicio, horarioFim, data, competencia, oficina)

# Herda de Usuario
class Colaborador(Usuario):

    def __init__(self, nome, senha, id, ocu, setor : str):
        super().__init__(nome, senha, id, ocu)
        self.__setor = setor
        self.__tercerizado = False
        self.__membro = False
        # retirei a caracteristica equipe pois não tem no diagrama

    def setTercerizado(self):
        self.__tercerizado = True

    def setMenbro(self):
        self.__membro = True

    def getColaborador(self):
        return f'{self.__setor}'

    def getsetor(self):
        return self.__setor 

# Herda de Colaborador
class ColabLider(Colaborador):

    def __init__(self, nome, senha, id, ocu, setor, eq):
        super().__init__(nome, senha, id, ocu, setor, eq)

    def gerenciamentoEvento(self, evento: Evento, titulo: str, horarioInicio: int, horarioFim: int, data: int, competencia, oficina):
        evento.setEvento(titulo, horarioInicio, horarioFim, data, competencia, oficina)

# Herda de Colaborador
class ColabMembro(Colaborador):

    def __init__(self, nome, senha, id, ocu, setor, eq):
        super().__init__(nome, senha, id, ocu, setor, eq)

class ComissaoOrg():
    def __init__(self,data : int, cargo : str, portaria : str) -> None:
        self.data = data
        self.cargo = cargo
        self.portaria = portaria

    def organizarEquipe():
        print('porfavor, informe os participantes da equipe:')
        with open('DB.txt', 'r') as arquivo:

            colabL = input('digite o colaborador líder:')
            colab1 = input('digite o colaborador:')
            colab2 = input('digite o colaborador:')
            colab3 = input('digite o colaborador:')

            lines = arquivo.readlines()

            for line in lines:
                if colabL in line and colab1 in line and colab2 in line and colab3 in line:
                    equipe = {
'Colaborador Líder' : colabL,
'Colaborador' : colab1,
'Colaborador' : colab2,
'Colaborador' : colab3
                    }
                    with open('equipes.txt', 'r') as arquivo:
                        arquivo.write(equipe,'\n')
                else: 
                    print('colaboradores não encontrados')

            return equipe
        
    def selecionarLocal(self,evento: Evento,nlocal: str):
        evento.setLocal(nlocal)
    # ------------------------ a desenvolver --------------------------------


# comentario para teste de push
