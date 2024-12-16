from classes import Admin, Colaborador, Usuario


def logon():
    dados = Usuario('', '', '', '')
    with open('DB.txt', 'a') as arquivo:
        choice = input("""
 Como deseja se cadastrar?

1 - Visitante
2 - Colaborador
3 - Administrador

R:""")

        if choice == '1' or 'VISITANTE' in choice.upper():
            try:
                nome, senha, id, ocup = dados.Collect(choice) # ------------------------ desenvolver a parte do colab e visitante (talvez passar eles direto como true e false com base no choice seja melhor)--------------------------------

                novovisit = Usuario(nome, senha, id, ocup)

                novovisit.setVisitante()

                arquivo.write(str(novovisit.getUsuario()) + '\n')
                print("Cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro no tipo de dado inserido: {e}")
                return None
            except TypeError as e:
                print(f"Erro no tipo de dado inserido: {e}")
                return None
            except Exception as e:
                print(f"Erro inesperado: {e}")
        elif choice == '2' or 'COLABORADOR' in choice.upper():
            try:
                nome, senha, id, ocup, setor = dados.Collect(choice)

                novocolab = Colaborador(nome, senha, id, ocup, setor)
                novocolab.setColab()
                choiceC = input("""
    Qual tipo de Colaborador você é?

    1 - Colaborador Líder
    2 - Colaborador Membro
    3 - Colaborador Tercerizado

    R:""")
                if choiceC == '1' or 'LÍDER' in choice.upper():                
                    arquivo.write(
                        str(novocolab.getUsuario()) + str(", ") + 
                        str(novocolab.getColaborador()) + '\n')
                    print("\nCadastrado com sucesso!")
                elif choiceC == '2' or 'MEMBRO' in choice.upper():
                    arquivo.write(
                        str(novocolab.getUsuario()) + str(", ") +
                        str(novocolab.getColaborador()) + '\n')
                    print("\nCadastrado com sucesso!")
                elif choiceC == '3' or 'TERCERIZADO' in choice.upper():
                    arquivo.write(
                        str(novocolab.getUsuario()) + str(", ") +
                        str(novocolab.getColaborador()) + '\n')
                    print("\nCadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro no tipo de dado inserido: {e}")
                return None
            except TypeError as e:
                print(f"Erro no tipo de dado inserido: {e}")
                return None
            except Exception as e:
                print(f"Erro inesperado: {e}")
        elif choice == '3' or 'ADMINISTRADOR' in choice.upper():
            try:
                nome, senha, id, ocup, setor = dados.Collect(choice)

                novoadm = Admin(nome, senha, id, ocup, setor)

                print(novoadm.getUsuario(), novoadm.getAdmin())

                arquivo.write(
                    str(novoadm.getUsuario()) + str(novoadm.getAdmin()) + '\n')
                print("Cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro no tipo de dado inserido: {e}")
                return None
            except TypeError as e:
                print(f"Erro no tipo de dado inserido: {e}")
                return None
            except Exception as e:
                print(f"Erro inesperado: {e}")
