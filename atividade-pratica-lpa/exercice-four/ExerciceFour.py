id = [1];  # Declaração de variaveis
name = None  # Declaração de variaveis
email = None  # Declaração de variaveis
phone = None  # Declaração de variaveis
course = None  # Declaração de variaveis
active = None  # Declaração de variaveis

while True:  # Laço whie True
    opcoes = input(
        "**********Menu**********\n 1 - Nova inscrição.\n 2 - Vizualizar inscrição.\n 0 - Encerrar.\n Opção Escolhida: ")  # Entrada de dados

    if (opcoes != "0" and opcoes != "1" and opcoes != "2") : # Condição para validar opção escolhida pelo user

        print("\nErro: digite uma opção válida!.\n")  # SPAN error
        continue # Instrução continue

    if (opcoes == "0"):  # Testando condição
        break

    if (opcoes == "1"):  # Testando condição
        for i in range(0, 10, 1):  # Laço de iteração
            id[i] += 1  # Incrementando vcariavel de iteração

            name = input("\n Informe seu nome: ")  # Entrada de dados
            email = input(" Informe seu email: ")  # Entrada de dados
            phone = input(" Informe seu telefone: ")  # Entrada de dados
            course = input(" Informe seu curso: ")  # Entrada de dados
            break
    if (opcoes == "2"):  # Testando condição
        if (name == None):  # Testando condição
            print("\n Nenhuma inscrição cadastrada!")  # Saida referente a falta de inscrições
            continue # Instrução continue
        else:
            print(
                "---------------LISTA DE INCRIÇÃO---------------\n Voucher: {}\n Nome: {}\n Email: {}\n Telefone: {}\n Curso: {}\n------------------------------".format(
                    id[0], name, email, phone, course)) # Saida referente a ficha de inscrições
