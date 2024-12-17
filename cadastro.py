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
            print(choice.upper().split())
            if '1' in choice.upper().split():
                # ------------------------ desenvolver a parte do colab e visitante (talvez passar eles direto como true e false com base no choice seja melhor)--------------------------------
                nome, senha, id, ocup = dados.Collect(choice)
                print(f"em dados: {nome, senha, id, ocup}")
                print(type(nome))
                # user = nome, senha, id, ocup
                # print(f"em user: {user}")
                with open('DB.txt', 'r') as arquivo:
                    lines = arquivo.readlines()
                    for line in lines:
                        if nome in line:
                            print('Você já está cadastrado\n')
                            return
                novovisit = Usuario(nome, senha, id, ocup)

                novovisit.setVisitante()

                arquivo.write(str(novovisit.getUsuario()) + '\n')
                print("Cadastrado com sucesso!33")
            elif choice == '2' or 'COLABORADOR' in choice.upper():
                nome, senha, id, ocup, setor = dados.Collect(choice)

                novocolab = Colaborador(nome, senha, id, ocup, setor)
                novocolab.setColab()
                choiceC = input("""
    Qual tipo de Colaborador você é?

    1 - Colaborador Líder
    2 - Colaborador Membro
    3 - Colaborador Tercerizado

    R:""")
                try:
                    if choiceC == '1' or 'LÍDER' in choice.upper():
                        arquivo.write(
                            str(novocolab.getUsuario()) + str(", ") +
                            str(novocolab.getColaborador()) + '\n')
                        print("\nCadastrado com sucesso!52")
                    elif choiceC == '2' or 'MEMBRO' in choice.upper():
                        arquivo.write(
                            str(novocolab.getUsuario()) + str(", ") +
                            str(novocolab.getColaborador()) + '\n')
                        print("\nCadastrado com sucesso!57")
                    elif choiceC == '3' or 'TERCERIZADO' in choice.upper():
                        arquivo.write(
                            str(novocolab.getUsuario()) + str(", ") +
                            str(novocolab.getColaborador()) + '\n')
                        print("\nCadastrado com sucesso!62")
                    else:
                        raise ValueError
                except ValueError:
                    print("\n Número inválido")
            elif choice == '3' or 'ADMINISTRADOR' in choice.upper():
                nome, senha, id, ocup, setor = dados.Collect(choice)

                novoadm = Admin(nome, senha, id, ocup, setor)

                print(novoadm.getUsuario(), novoadm.getAdmin())

                arquivo.write(
                    str(novoadm.getUsuario()) + str(novoadm.getAdmin()) + '\n')
                print("Cadastrado com sucesso!76")
            else:
                raise ValueError
        except ValueError:
            print("\n Número inválido")