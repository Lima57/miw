def Acess():
    with open('C:\\Users\\Aluno\\miw\\Miw\\DB.txt', 'r') as arquivo:
        Login = False

        user = input('digite seu usuário:')
        keyworld = input('digite sua senha:')

        lines = arquivo.readlines()

        for line in lines:
            if user in line and keyworld in line:
                Login = True
                print('Login efetuado com sucesso\n')
                break

        print('Login incorreto\n')
        return Login
