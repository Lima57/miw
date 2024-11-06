from abc import ABC, abstractmethod


# usuários:

# coordenador
# colaborador
# colab lider
# colab membro
# colab tercerizado
# participante


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
    def setnome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("O nome deve ser uma string.")

    @senha.setter
    def setsenha(self, senha):
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
    def __init__ (self, descricao: str, regras: str, limite_participantes: int, identificacao_participante: int ):
        self.descricao = descricao
        self.regras = regras
        self.limite_participantes = limite_participantes
        self.identificacao_participante = identificacao_participante

#Criei uma intancia da classe com o metodo __init__
competicao = Competicao("Competição do Orgulho Nerd", "Seguir as instruções do evento.", 200, 1)

class Oficina():
    def __init__ (self, descricao: str, limite: int):
        self.descricao = descricao
        self.limite = limite

oficina = Oficina("Oficina de Cosplay", 50)

print("Descrição: ", oficina.descricao)
print("Limite de participantes: ", oficina.limite)

class Evento:
    def __init__(self, titulo: str, horarioInicio: int, horarioFim: int, data: int, local: str, competencia : bool, oficina : bool):
        self.titulo = titulo
        self.horarioInicio = horarioInicio
        self.horarioFim = horarioFim
        self.data = data
        self.local = local
        self.competencia = competencia
        self.oficina = oficina
        self.participantes = []

    def setEvento(self, titulo: str, horarioInicio: int, horarioFim: int, data: int):
        self.titulo = titulo
        self.horarioInicio = horarioInicio
        self.horarioFim = horarioFim
        self.data = data

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
Local: {self.local}
''')

    def inscricaoOficina(self):
        self.oficina = True

    def inscricaoComp(self):
        self.competencia = True

    def emissaoCertificado(self):
        print('certificado emitido')

    def gerenciamentoEvento(self, evento, titulo: str, horarioInicio: int, horarioFim: int, data: int):
        evento.setEvento(titulo, horarioInicio, horarioFim, data)
        
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

class ColabLider(Colaborador):

    def __init__(self, nome, senha, id, ocu, setor, eq):
        super().__init__(nome, senha, id, ocu, setor, eq)

    def gerenciamentoEvento(self, evento: Evento, titulo: str, horarioInicio: int, horarioFim: int, data: int, competencia, oficina):
        evento.setEvento(titulo, horarioInicio, horarioFim, data, competencia, oficina)

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
