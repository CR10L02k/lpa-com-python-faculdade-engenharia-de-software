nome = None # Declaração da variavel.

nome  = input("\n - Digite um nome: ")  # Declarando e e armaenando dados na variavel.

nome = nome.upper() # Tranformando os caracteres da String para UPPER CASE.
nome = nome.replace("A", "@") # Metodo responsavel pela substituição dos caracteres contidos nos argumentos do mesmo.
nome = nome.replace("E", "&") # Metodo responsavel pela substituição dos caracteres contidos nos argumentos do mesmo.
nome = nome.replace("I", "!") # Metodo responsavel pela substituição dos caracteres contidos nos argumentos do mesmo.
nome = nome.replace("O", "#") # Metodo responsavel pela substituição dos caracteres contidos nos argumentos do mesmo.
nome = nome.replace("U", "*") # Metodo responsavel pela substituição dos caracteres contidos nos argumentos do mesmo.

print("\n - {}".format(nome)) # Imprimindo resultado final da variavel no console.
