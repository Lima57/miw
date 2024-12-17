'''
GRUPO: miw /// Turma: 2A
Alunos: Kaio de Lima, Marcos Vinnicius, Guilherme Albuquerque, Vitória Shailia
Professora: Camila Serrão
'''
from cadastro import logon
import classes

eventos = [classes.Evento('Evento de UNO', 14, 15, 14112024,"sala 10", True, False), classes.Evento('Evento de Pokémon', 16, 17, 14112024,'sala 11', True, False)]
#teste
def menu():
    permission = None
    while True:
        try:
            if permission == None or permission == False:
                print('''
    1 - Login
    2 - Cadastro
    3 - Encerrar sessão
    ''')
                choice = input('R:')
                if choice == '1' or 'LOGIN' in choice.upper().split():
                    with open('DB.txt', 'r') as arquivo:

                        user = input('digite seu usuário:')
                        keyworld = input('digite sua senha:')

                        lines = arquivo.readlines()

                        for line in lines:
                            if user in line and keyworld in line:
                                permission = True
                                print('Login efetuado com sucesso\n')

                        print('Login incorreto\n')

                elif choice == '2' or 'CADASTRO' in choice.upper().split():
                    logon()
                elif choice == '3' or 'ENCERRAR' in choice.upper().split():
                    break
                else:
                    raise ValueError

            elif permission:
                print('''
    1 - Cadastro
    2 - Sair de conta
    3 - Encerrar sessão
    4 - Ver eventos
    5 - Inscrição de evento
    6 - Gerenciar evento
    ''')
                choice = input('R:')
                if choice == '1' or 'CADASTRO' in choice.upper().split():
                    logon()
                elif choice == '2' or 'SAIR' in choice.upper().split():
                    permission = False
                elif choice == '3' or 'ENCERRAR SESSÃO' in choice.upper().split():
                    break
                elif choice == '4' or 'VER EVENTOS' in choice.upper().split():
                    for object in range(len(eventos)):
                        eventos[object].getEvento()
                        input('Aperte enter para continuar ')

                elif choice == '5' or 'INSCRIÇÃO DE EVENTO' in choice.upper().split():
                    print('Escolha o evento de inscrição: ')
                    for object in range(len(eventos)):
                        print(f'{object + 1} - {eventos[object].getTitulo()}')

                    inscri = int(input('Número do evento: '))

                    if 0 <= inscri <= len(eventos):
                        eventos[inscri - 1].addParticipante(permission)
                        print('Participante Cadastrado')
                    else:
                        print('\n Número inválido')

                elif choice == '6' or 'GERENCIAR EVENTO':
                    print('Faça o login como Admin para gerenciar evento (há por padrão um adm salvo no código): ')
                    with open('DB.txt', 'r') as arquivo:

                        user = input('Digite o usuário: ')
                        keyworld = input('Digite a senha: ')

                        lines = arquivo.readlines()

                        for line in lines:
                            if user in line and keyworld in line:
                                print('Deseja editar qual evento? ')
                                for object in range(len(eventos)):
                                    print(f'{object + 1} - {eventos[object].getTitulo()}')

                                try:
                                    escolha = int(input("Escolha o número do evento para gerenciar: ")) - 1
                                    if 0 <= escolha < len(eventos):
                                        evento_selecionado = eventos[escolha]
                                        # Chama o método gerenciamentoEvento do evento selecionado
                                        titulo = input('Novo Título:')
                                        horarioI = input('Novo Horario de Inicio:')
                                        horarioF = input('Novo Horario Final:')
                                        data = input('Nova data:')

                                        evento_selecionado.gerenciamentoEvento(evento_selecionado,titulo, horarioI, horarioF, data)

                                    else:
                                        print("Opção inválida.")
                                except ValueError:
                                    print("Entrada inválida. Por favor, insira um número inteiro.")
                                else:
                                    print('Evento gerenciado com sucesso!')
                else:
                    raise ValueError('Insira um número válido.')

        except ValueError:
            print('Erro; valor não permitido.')
        finally:
            print('Loop terminado.')

menu()
