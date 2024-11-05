def Acess():
    infouser = []
    with open('C:\\Users\\Aluno\\miw\\Miw\\DB.txt', 'r') as arquivo:
        Login = False

        user = input('digite seu usuário:')
        infouser.append(user)
        keyworld = input('digite sua senha:')
        infouser.append(keyworld)
        
        lines = arquivo.readlines()

        for line in lines:
            if user in line and keyworld in line:
                Login = True
                print('Login efetuado com sucesso\n')
                break

        print('Login incorreto\n')
        return Login
