'''
GRUPO: miw /// Turma: 2A
Alunos: Kaio de Lima, Marcos Vinnicius, Guilherme Albuquerque, Vitória Shailia
Professora: Camila Serrão
'''
from cadastro import logon
from login import Acess
import classes

oficinagenerica = classes.Oficina('Título', 10)
competicaogenerica = classes.Competicao('Título', 10)
eventoON = [classes.Evento('Orgulho Nerd', 14, 15, 14112024, oficinagenerica, competicaogenerica), classes.Evento('Evento de Pokémon', 16, 17, 14112024, True, False)]
oficinas = [classes.Oficina('Oficina de Programação', 40), classes.Oficina('Oficina de Cultura Pop', 40)]
competicoes = [classes.Competicao('Competição de Cosplay', 15), classes.Competicao('Competição Pokémon TCG', 40)]

def menu():
    permission = None
    while True:
        if permission == None or permission == False:
            print('''
1 - Login
2 - Cadastro
3 - Encerrar sessão
''')
            choice = input('R:')
            if choice == '1' or 'LOGIN' in choice.upper().split():
                permission = Acess()
            elif choice == '2' or 'CADASTRO' in choice.upper().split():
                logon()
            elif choice == '3' or 'ENCERRAR' in choice.upper().split():
                break
            else:
                print('Opção inválida')

        elif permission:
            print('''
1 - Cadastro
2 - Sair de conta
3 - Encerrar sessão
4 - Ver oficinas
5 - Ver competições
6 - Inscrição de evento
7 - Inscrição de oficina
8 - Inscrição de competição
''')
            choice = input('R:')
            if choice == '1' or 'CADASTRO' in choice.upper().split():
                logon()
            elif choice == '2' or 'SAIR' in choice.upper().split():
                permission = False
            elif choice == '3' or 'ENCERRAR SESSÃO' in choice.upper().split():
                break
            elif choice == '4' or 'VER OFICINAS' in choice.upper().split():
                for object in range(len(oficinas)):
                    oficinas[object].getDescricaoOfic()
                    input('aperte enter para continuar')
            elif choice == '5' or 'VER COMPETIÇÕES' in choice.upper().split():
                for object in range(len(competicoes)):
                    competicoes[object].getDescricaoComp()
                    input('aperte enter para continuar')

            elif choice == '6' or 'INSCRIÇÃO DE EVENTO' in choice.upper().split():
                print('Escolha o evento de inscrição:')
                for object in range(len(eventoON)):
                    print(f'{object + 1} - {eventoON[object].getTitulo()}')

                inscri = int(input('numero do evento:'))

                if inscri <= len(eventoON):
                    eventoON[inscri - 1].addParticipante(permission)
                    print('Participante Cadastrado')
                else:
                    print('\n Número inválido')

            elif choice == '7' or 'INSCRIÇÃO DE OFICINA' in choice.upper().split():
                print('Escolha a oficina em que irá se inscrever:')
                for object in range(len(oficinas)):
                    print(f'{object + 1} - {oficinas[object].getDescricaoOfic()}')

                inscriofi = int(input('numero do evento:'))

                if inscriofi <= len(oficinas):
                    oficinas[inscriofi - 1].addParticipanteOfic(permission)
                    print('Participante Cadastrado')
                else:
                    print('\n Número inválido')

            elif choice == '8' or 'INSCRIÇÃO DE COMPETIÇÃO' in choice.upper().split():
                print('Escolha a competição em que irá se inscrever:')
                for object in range(len(competicoes)):
                    print(f'{object + 1} - {competicoes[object].getDescricaoComp()}')

                inscricom = int(input('numero do evento:'))

                if inscricom <= len(competicoes):
                    competicoes[inscricom - 1].addParticipanteComp(permission)
                    print('Participante Cadastrado')
                else:
                    print('\n Número inválido')
menu()
