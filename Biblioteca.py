while True:
    #Menu de opções: Menu que dará opções das opçãos do sistema que deseja realizar.
    print("\nMenu de opções: \n1- Cadastrar livro \n2 - Verificar disponibilidade do livro \n3 - Solicitar emprestimo de livro \n4 - Devolução de livro \n5 - Livros cadastrados \n6 - Finalizar")
    opcao = int(input("Escolha a opção desejada de acordo com o menu acima: "))

    match opcao:
        #Cadastro do livro: menu que será feito o cadastro dos livros da Biblioteca
        case 1:
           livro1 = input("\nNome do livro: ")
           autor1 = input("Autor do livro: ")
           anofabricacao1 = int(input("Ano de fabricação do livro: "))
           dispon1 = "disponível"

           livro2 = input("\nNome do livro: ")
           autor2 = input("Autor do livro: ")
           anofabricacao2 = int(input("Ano de fabricação do livro: "))
           dispon2 = "disponível"
           
           livro3 = input("\nNome do livro: ")
           autor3 = input("Autor do livro: ")
           anofabricacao3 = int(input("Ano de fabricação do livro: "))
           dispon3 = "disponível"
           
           livro4 = input("\nNome do livro: ")
           autor4 = input("Autor do livro: ")
           anofabricacao4 = int(input("Ano de fabricação do livro: "))
           dispon4 = "disponível"
           
           livro5 = input("\nNome do livro: ")
           autor5 = input("Autor do livro: ")
           anofabricacao5 = int(input("Ano de fabricação do livro: "))
           dispon5 = "disponível"
        
        case 2:
            #Menu de verificação de disponibilidade: menu que faz a verificação da disponibilidade do livro na Biblioteca.
            if dispon1 == "disponível":
                print(f"\nO livro {livro1} está disponível na Biblioteca")
            else:
                print(f"O livro {livro1} não está disponível na Biblioteca")
            
            if dispon2 == "disponível":
                print(f"O livro {livro2} está disponível na Biblioteca")
            else:
                print(f"O livro {livro2} não está disponível na Biblioteca")
            
            if dispon3 == "disponível":
                print(f"O livro {livro3} está disponível na Biblioteca")
            else:
                print(f"O livro {livro3} não está disponível na Biblioteca")
            
            if dispon4 == "disponível":
                print(f"O livro {livro4} está disponível na Biblioteca")
            else:
                print(f"O livro {livro4} não está disponível na Biblioteca")
            
            if dispon5 == "disponível":
                print(f"O livro {livro5} está disponível na Biblioteca")
            else:
                print(f"O livro {livro5} não está disponível na Biblioteca")
        
        case 3:
            #Menu de emprestimo do livro: menu que fará o registro do emprestimo do livro da Biblioteca.
            emprestimo = input("Qual o nome do livro que deseja emprestado: ")

            if emprestimo == livro1:
                dispon1 = "emprestado"
            
            if emprestimo == livro2:
                dispon2 = "emprestado"

            if emprestimo == livro3:
                dispon3 = "emprestado"
            
            if emprestimo == livro4:
                dispon4 = "emprestado"
   
            if emprestimo == livro5:
                dispon5 = "emprestado"

        case 4:
            #Menu de devolução do livro: menu que fará o registro da devolução do livro da Biblioteca.
            devolucao = input("Qual o nome do livro que deseja devolver: ")

            if devolucao == livro1:
                dispon1 = "disponível"
            
            if devolucao == livro2:
                dispon2 = "disponível"

            if devolucao == livro3:
                dispon3 = "disponível"
            
            if devolucao == livro4:
                dispon4 = "disponível"
   
            if devolucao == livro5:
                dispon5 = "disponível"

        case 5:
            #Menu de informação do cadastro do livro: menu que mostra a informação de cadastro dos livros da Biblioteca.
            print(f"Livros cadastrados: \nLivro: {livro1} \tAutor: {autor1} \tAno de fabricação: {anofabricacao1}")
            print(f"Livro: {livro2} \tAutor: {autor2} \tAno de fabricação: {anofabricacao2}")
            print(f"Livro: {livro3} \tAutor: {autor3} \tAno de fabricação: {anofabricacao3}")
            print(f"Livro: {livro4} \tAutor: {autor4} \tAno de fabricação: {anofabricacao4}")
            print(f"Livro: {livro5} \tAutor: {autor5} \tAno de fabricação: {anofabricacao5}")

        case 6:
            #Finalização do programa.
            print("Finalizando..........")

            break



