from classes import Admin, Colaborador, Usuario


def logon():
    dados = Usuario('', '', '', '')
    cadastrado = None
    with open('DB.txt', 'a') as arquivo:
        choice = input("""
 Como deseja se cadastrar?

1 - Visitante
2 - Colaborador
3 - Administrador

R:""")
        try:
            if '1' in choice.upper().split() or 'VISITANTE' in choice.upper():

                nome, senha, id, ocup = dados.Collect(choice)

                user = f"{nome}, {senha}, {id}, {ocup}"
                with open('DB.txt', 'r') as arquivo:
                    lines = arquivo.readlines()
                    for line in lines:
                        if user.strip() == line.strip():  
                            print("Você já está cadastrado.\n")
                            return
                novovisit = Usuario(nome, senha, id, ocup)

                novovisit.setVisitante()
                with open('DB.txt', 'a') as arquivo:
                    arquivo.write(str(novovisit.getUsuario()) + '\n')
                print("Cadastrado com sucesso!")
            elif '2' in choice.upper().split() or 'COLABORADOR' in choice.upper():
                nome, senha, id, ocup, setor = dados.Collect(choice)

                user = f"{nome}, {senha}, {id}, {ocup}, {setor}"
                with open('DB.txt', 'r') as arquivo:
                    lines = arquivo.readlines()
                    for line in lines:
                        if user.strip() == line.strip():  
                            print("Você já está cadastrado.\n")
                            return

                novocolab = Colaborador(nome, senha, id, ocup, setor)
                novocolab.setColab()
                choiceC = input("""
    Qual tipo de Colaborador você é?

    1 - Colaborador Líder
    2 - Colaborador Membro
    3 - Colaborador Tercerizado

    R:""")
                try:
                    if '1' in choiceC.upper().split() or 'LÍDER' in choiceC.upper():
                        with open('DB.txt', 'a') as arquivo:
                            arquivo.write(
                                str(novocolab.getUsuario()) + str(", ") +
                                str(novocolab.getColaborador()) + '\n')
                        print("\nCadastrado com sucesso!")
                    elif '2' in choiceC.upper().split() or 'MEMBRO' in choiceC.upper():
                        with open('DB.txt', 'a') as arquivo:
                            arquivo.write(
                                str(novocolab.getUsuario()) + str(", ") +
                                str(novocolab.getColaborador()) + '\n')
                        print("\nCadastrado com sucesso!")
                    elif '3' in choiceC.upper().split() or 'TERCERIZADO' in choiceC.upper():
                        with open('DB.txt', 'a') as arquivo:
                            arquivo.write(
                                str(novocolab.getUsuario()) + str(", ") +
                                str(novocolab.getColaborador()) + '\n')
                        print("\nCadastrado com sucesso!")
                    else:
                        raise ValueError
                except ValueError:
                    print("\n Número inválido")
            elif '3' in choice.upper().split() or 'ADMINISTRADOR' in choice.upper():
                nome, senha, id, ocup, setor = dados.Collect(choice)

                user = f"{nome}, {senha}, {id}, {ocup}, {setor}"
                with open('DB.txt', 'r') as arquivo:
                    lines = arquivo.readlines()
                    for line in lines:
                        if user.strip() == line.strip():  
                            print("Você já está cadastrado.\n")
                            return

                novoadm = Admin(nome, senha, id, ocup, setor)

                with open('DB.txt', 'a') as arquivo:
                    arquivo.write(
                        str(novoadm.getUsuario()) + str(novoadm.getAdmin()) + '\n')
                print("Cadastrado com sucesso!")
            else:
                raise ValueError
        except ValueError:
            print("\n Número inválido")
