print("\n   HOTEL DOS ANIMAIS")  # Saida de dados
print(
    "\n --> Um hotel onde os hóspedes têm algumas restrições quanto a localização do seu quarto, seguindo as seguintes regras:")  # Saida de dados
print(
    "\n O rato não pode ficar ao lado do gato\n O cão não pode ficar ao lado do osso.\n O gato não pode ficar ao lado do cão.\n O queijo não pode ficar ao lado do rato.\n")  # Saida de dados
print(" Especificando posiões: \n     [1, 2, 3, 4]\n     [5, 6, 7, 8]\n")  # Saida de dados
print(" Bem vindo a Fase 1!")  # Saida de dados

print(
    "Na primeira fase o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos:\n")  # Saida de dados
print("['*', '*', '_', 'G']\n['R', '_', '*', '*']")  # Saida de dados

posicaoGato = input(
    "\n Em qual posição quer alocar o GATO? -> ")  # Saida e entrada de dados e guadando valor na variavel.
posicaoRato = input(
    " Em qual posição quer alocar o RATO? -> ")  # Saida e entrada de dados e guadando valor na variavel.

if ((posicaoGato != "3") or (posicaoRato != "6")):  # Condição para game over
    print("\n Você perdeu!")  # Saida de dados

else:  # Caso a condição do if não seja satisfeita ela cai no else que informa que o user ganhou.

    print("\n Você ganhou!")  # Saida de dados
    print("\n Bem vindo a Fase 2!\n")  # Saida de dados

    print(
        "Na segunda fase o jogador deve alocar o CÃO, CÃO E OSSO na seguinte matriz que representa os quartos:\n")  # Saida de dados
    print("['_', '*', '*', '*']\n['*', 'C', '_', '_']")  # Saida de dados

    posicaoCao = input(
        " Em qual posição quer alocar o primeiro CÃO? -> ")  # Saida e entrada de dados e guadando valor na variavel.
    posicaoCaoDois = input(
        " Em qual posição quer alocar o segundo CÃO? -> ")  # Saida e entrada de dados e guadando valor na variavel.
    posicaoOsso = input(
        " Em qual posição quer alocar o OSSO? -> ")  # Saida e entrada de dados e guadando valor na variavel.

    if ((posicaoCao != "7" and posicaoCao != "8") or (posicaoCaoDois != "7" and posicaoCaoDois != "8") or (
            posicaoOsso != "1")):  # Condição para game over
        print("\n Você perdeu!")  # Saida de dados

    else:  # Caso a condição do if não seja satisfeita ela cai no else que informa que o user ganhou.

        print("\n Você ganhou!")  # Saida de dados
        print("\n Bem vindo a Fase 3!\n")  # Saida de dados

        print(
            "Na terceira fase o jogador deve alocar o GATO, RATO E OSSO na seguinte matriz que representa os quartos:\n")  # Saida de dados
        print("['_', '*', '*', '*']\n['_', 'G', '_', '*']")  # Saida de dados

        posicaoGato = input(
            "\n Em qual posição quer alocar o GATO? -> ")  # Saida e entrada de dados e guadando valor na variavel.
        posicaoRato = input(
            " Em qual posição quer alocar o RATO? -> ")  # Saida e entrada de dados e guadando valor na variavel.
        posicaoOsso = input(
            " Em qual posição quer alocar o OSSO? -> ")  # Saida e entrada de dados e guadando valor na variavel.

        if ((posicaoRato != "1") or (posicaoGato != "7") or (posicaoOsso != "5")):  # Condição para game over
            print("\n Você perdeu!")  # Saida de dados

        else:  # Caso a condição do if não seja satisfeita ela cai no else que informa que o user ganhou.

            print("\n Você ganhou!")  # Saida de dados
            print("\n Bem vindo a Fase 4!\n")  # Saida de dados

            print(
                "Na quarta fase o jogador deve alocar o QUEIJO, QUEIJO E OSSO na seguinte matriz que representa os quartos:\n")  # Saida de dados
            print("['_', '_', '_', '*']\n['*', 'R', '*', '*']")  # Saida de dados

            posicaoQueijo = input(
                "\n Em qual posição quer alocar o QUEIJO? -> ")  # Saida e entrada de dados e guadando valor na variavel.
            posicaoQueijoDois = input(
                " Em qual posição quer alocar o segundo QUEIJO? -> ")  # Saida e entrada de dados e guadando valor na variavel.
            posicaoOsso = input(
                " Em qual posição quer alocar o OSSO? -> ")  # Saida e entrada de dados e guadando valor na variavel.

            if (posicaoOsso != "2"):  # Condição para game over
                print("\n Você perdeu!")  # Saida de dados

            else:  # Caso a condição do if não seja satisfeita ela cai no else que informa que o user ganhou.

                print("\n Você ganhou!")  # Saida de dados
                print("\n Parabéns, passou por todas a fases!\n")  # Saida de dados
