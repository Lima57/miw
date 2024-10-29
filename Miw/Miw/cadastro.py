from classes import Admin, ColabLider, Colaborador, Usuario, Visitante


def logon():
    dados = Usuario('', '', '', '')
    with open('DB.txt', 'a') as arquivo:
        choice = input("""
 Como deseja se cadastrar?

1 - Visitante
2 - Colaborador
3 - Colaborador Líder
4 - Colaborador Membro
5 - Colaborador Tercerizado
6 - Administrador

R:""")

        if choice == '1' or 'VISITANTE' in choice.upper():
            nome, senha, id, ocup = dados.Collect(choice) # ------------------------ desenvolver a parte do colab e visitante (talvez passar eles direto como true e false com base no choice seja melhor)--------------------------------

            novovisit = Visitante(nome, senha, id, ocup)

            print(novovisit.getUsuario())

            arquivo.write(str(novovisit.getUsuario()) + '\n')
        elif choice == '2' or 'COLABORADOR' in choice.upper():
            nome, senha, id, ocup, setor, equipe = dados.Collect(choice)

            novocolab = Colaborador(nome, senha, id, ocup, setor, equipe)

            print(novocolab.getUsuario(), novocolab.getColaborador())

            arquivo.write(
                str(novocolab.getUsuario()) + str(novocolab.getColaborador()) +
                '\n')
        elif choice == '3' or 'LÍDER' in choice.upper():
            nome, senha, id, ocup, setor, equipe = dados.Collect(choice)

            novocolabL = ColabLider(nome, senha, id, ocup, setor, equipe)

            print(novocolabL.getUsuario(), novocolabL.getColaborador())

            arquivo.write(
                str(novocolabL.getUsuario()) +
                str(novocolabL.getColaborador()) + '\n')
        elif choice == '4' or 'MEMBRO' in choice.upper():
            nome, senha, id, ocup, setor, equipe = dados.Collect(choice)

            novocolabM = ColabLider(nome, senha, id, ocup, setor, equipe)

            print(novocolabM.getUsuario(), novocolabM.getColaborador())

            arquivo.write(
                str(novocolabM.getUsuario()) +
                str(novocolabM.getColaborador()) + '\n')
        elif choice == '5' or 'TERCERIZADO' in choice.upper():
            nome, senha, id, ocup, setor, equipe = dados.Collect(choice)

            novocolabT = ColabLider(nome, senha, id, ocup, setor, equipe)

            print(novocolabT.getUsuario(), novocolabT.getColaborador())

            arquivo.write(
                str(novocolabT.getUsuario()) +
                str(novocolabT.getColaborador()) + '\n')
        elif choice == '6' or 'ADMINISTRADOR' in choice.upper():
            nome, senha, id, ocup, setor = dados.Collect(choice)

            novoadm = Admin(nome, senha, id, ocup, setor)

            print(novoadm.getUsuario(), novoadm.getAdmin())

            arquivo.write(
                str(novoadm.getUsuario()) + str(novoadm.getAdmin()) + '\n')
