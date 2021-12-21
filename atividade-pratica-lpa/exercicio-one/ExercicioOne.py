nome = None # Declaração de varieveis.
idade = None # Declaração de varieveis.
opcao = None # Declaração de varieveis.

while (True) : # Bloco While. Responsavel pelo loop do programa.

    nome = input("\n - Nome da criança: ") # Variavel para coleta de dados
    idade = int(input("\n  - Informe a idade da mesma: ")) # Variavel para coleta de dados

    if (idade >= 1 and idade <= 5) : # Condicionais para validação da idade.
        print("\n - A aluno(a) {} tem {} e está no ensino infantil.".format(nome, idade)) # Impressão do resultado no console.

    if (idade >= 6 and idade <= 10) : # Condicionais para validação da idade.
        print("\n - A aluno(a) {} tem {} e está no ensino fundamental I.".format(nome, idade)) # Impressão do resultado no console.

    if (idade >= 11 and idade <= 14) : # Condicionais para validação da idade.
        print("\n - A aluno(a) {} tem {} e está no ensino fundamental II.".format(nome, idade)) # Impressão do resultado no console.

    if (idade >= 15) : # Condicionais para validação da idade.
        print("\n - A aluno(a) {} tem {} e está no ensino médio.".format(nome, idade)) # Impressão do resultado no console.

    opcao = input("\n - Deseja continuar? 0 - Não 1 - Sim") # Coletando dado para decisão de continuação ou encerramento do programa.

    if (opcao == 0 or not opcao.isnumeric()) : # Condição para encerrar o programa, caso a mesma seja satisfeita.
        break # Metodo responsavel por encerrar o programa.
