'''
GRUPO: miw /// Turma: 2A
Alunos: Kaio de Lima, Marcos Vinnicius, Guilherme Albuquerque, Vitória Shailia
Professora: Camila Serrão
'''
from cadastro import logon
from login import Acess


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
            if choice == '1' or 'LOGIN' in choice.upper():
                permission = Acess()
            elif choice == '2' or 'CADASTRO' in choice.upper():
                logon()
            elif choice == '3' or 'ENCERRAR' in choice.upper():
                break
            else:
                print('Opção inválida')

        elif permission == True:
            print('''
1 - Cadastro
2 - Sair de conta
3 - Encerrar sessão
4 - "Opções de administrador"
''')
            choice = input('R:')
            if choice == '1' or 'CADASTRO' in choice.upper():
                cadastro.logon()
            elif choice == '2' or 'SAIR' in choice.upper():
                permission = False
            elif choice == '3' or 'ENCERRAR SESSÃO' in choice.upper():
                break
            elif choice == '4':
                print('opção em desenvolvimento')


menu()
