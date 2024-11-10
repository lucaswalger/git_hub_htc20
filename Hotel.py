quarto101 = "disponível"
quarto102 = "disponível"
quarto103 = "disponível"
quarto104 = "disponível"
quarto105 = "disponível"

while True:
    #Menu de opções: Menu que dará opções das opçãos do sistema que deseja realizar.
    print("\nMenu de opções: \n1- Cadastrar hóspede \n2 - Verificar disponibilidade do quarto \n3 - Registro de entrada \n4 - Registro de saída \n5 - Hospedes cadastrados \n6 - Retirada de reserva \n7 - Finalizar")
    opcao = int(input("Escolha a opção desejada de acordo com o menu acima: "))

    match opcao:
        case 1:
           #Menu de cadastro  de hóspedes: menu  aonde  irá ser feito o registro de cada hóspede no quarto desejado.
           if quarto101 == "disponível":
            hospede1 = input("\nNome do hóspede: ")
            dataentrada1 = input("Data da entrada do hóspede: ")
            datasaida1 = input("Data de saida do hóspede: ")
            quarto101 = "reservado"

           if quarto102 == "disponível":
            hospede2 = input("\nNome do hóspede: ")
            dataentrada2 = input("Data da entrada do hóspede: ")
            datasaida2 = input("Data de saida do hóspede: ")
            quarto102 = "reservado"
           
           if quarto103 == "disponível":
            hospede3 = input("\nNome do hóspede: ")
            dataentrada3 = input("Data da entrada do hóspede: ")
            datasaida3 = input("Data de saida do hóspede: ")
            quarto103 = "reservado"
           
           if quarto104 == "disponível":
            hospede4 = input("\nNome do hóspede: ")
            dataentrada4 = input("Data da entrada do hóspede: ")
            datasaida4 = input("Data de saida do hóspede: ")
            quarto104 = "reservado"
           
           if quarto105 == "disponível":
            hospede5 = input("\nNome do hóspede: ")
            dataentrada5 = (input("Data da entrada do hóspede: "))
            datasaida5 = (input("Data de saida do hóspede: "))
            quarto105 = "reservado"
        
        case 2:
            #Menu de verificação de disponibilidade de quarto: menu aonde será feito a verificação dos quartos disponiveis para ser cadastrado o hóspede.
            if quarto101 == "disponível":
                print(f"\nQuarto 101 está disponível")
            elif quarto101 == "reservado":
                print(f"\nQuarto 101 está reservado")
            else:
                print(f"\nQuarto 101 não está disponível")
            
            if quarto102 == "disponível":
                print(f"\nQuarto 102 está disponível")
            elif quarto102 == "reservado":
                print(f"\nQuarto 101 está reservado")
            else:
                print(f"\nQuarto 102 não está disponível")
            
            if quarto103 == "disponível":
                print(f"\nQuarto 103 está disponível")
            elif quarto103 == "reservado":
                print(f"\nQuarto 101 está reservado")
            else:
                print(f"\nQuarto 103 não está disponível")
            
            if quarto104 == "disponível":
                print(f"\nQuarto 104 está disponível")
            elif quarto104 == "reservado":
                print(f"\nQuarto 101 está reservado")
            else:
                print(f"\nQuarto 104 não está disponível")
            
            if quarto105 == "disponível":
                print(f"\nQuarto 105 está disponível")
            elif quarto105 == "reservado":
                print(f"\nQuarto 101 está reservado")
            else:
                print(f"\nQuarto 105 não está disponível")
        
        case 3:
            #Menu de registro de entrada: menu aonde será feito o registro de entrada do hóspede cadastrado no hotel e deixara o quarto que ele reservou indisponível.
            entrada = input("Nome do hóspede para registro de entrada: ")
            
            if entrada == hospede1:
                print(f"\nEntrada registada para {entrada} com sucesso")
                quarto101 = "indisponível"
            
            elif entrada == hospede2:
               print(f"\nEntrada registada para {entrada} com sucesso")
               quarto102 = "indisponível"

            elif entrada == hospede3:
               print(f"\nEntrada registada para {entrada} com sucesso")
               quarto103 = "indisponível"

            elif entrada == hospede4:
               print(f"\nEntrada registada para {entrada} com sucesso")
               quarto104 = "indisponível"

            elif entrada == hospede5:
               print(f"\nEntrada registada para {entrada} com sucesso")      
               quarto105 = "indisponível"

            else:
                print(f"\nHóspede {entrada} não encontrado")
        
        case 4:
            #Registro de saída: menu aonde será registrado a saída do hóspede cadastrado no hotel e disponibilizara o quarto que ele hospedou.
            saida = input("Nome do hóspede para registro de saída: ")
            
            if saida == hospede1:
                print(f"\nSaída registada para {saida} com sucesso")
                quarto101 = "disponível"
            
            elif saida == hospede2:
                print(f"\nSaída registada para {saida} com sucesso")
                quarto102 = "disponível"

            elif saida == hospede3:
              print(f"\nSaída registada para {saida} com sucesso")
              quarto103 = "disponível"
            
            elif saida == hospede4:
                print(f"\nSaída registada para {saida} com sucesso")
                quarto104 = "disponível"

            elif saida == hospede5:
                print(f"\nSaída registada para {saida} com sucesso")
                quarto105 = "disponível"    

            else:
                print(f"\nHóspede {saida} não encontrado")

        case 5:
            #Menu de informação do hóspede: menu que mostra as informações de cadastro que foram realizada para o hóspede.
            print(f"Hóspedes cadastrados: \nHospede: {hospede1} \tQuarto: 101 \tData de entrada: {dataentrada1} \tData de saida: {datasaida1}")
            print(f"Hóspede: {hospede2} \tQuarto: 102 \tData de entrada: {dataentrada2} \tData de saida: {datasaida2}")
            print(f"Hóspede: {hospede3} \tQuarto: 103 \tData de entrada: {dataentrada3} \tData de saida: {datasaida3}")
            print(f"Hóspede: {hospede4} \tQuarto: 104 \tData de entrada: {dataentrada4} \tData de saida: {datasaida4}")
            print(f"Hóspede: {hospede5} \tQuarto: 105 \tData de entrada: {dataentrada5} \tData de saida: {datasaida5}")

        case 6:
           #Menu de verificação de comparececimento: menu que faz a verificação se o hóspede apareceu no dia de entrada cadastrado.
           if quarto101 == "reservado":
             naoapareceu = input("Hospede apareceu para registro de entrada:(S/N) ")
             
             if naoapareceu == "N" or naoapareceu == "n":
                removerreserva = input("Deseja remover reserva:(S/N)")
             else:
                print("Retornando para o Menu......")

             if removerreserva == "S" or removerreserva == "s":
                 print("Removendo reserva.........")
                 quarto101 = "disponível"
             else:
                alteradataentrada = input("Deseja mudar a data de entrada:(S/N) ")
                alteradatasaida = input("Deseja mudar a data de saida:(S/N)")
             
             if alteradataentrada == "S" or alteradataentrada == "s" and alteradatasaida == "S" or alteradatasaida == "s":
                dataentrada1 = input("Para quando deseja alterar a data de entrada: ")
                datasaida1 = input("Para quando deseja alterar a data de saida: ")
             else:
                print("Retornando ao menu......")

           if quarto102 == "reservado":
             naoapareceu = input("Hospede apareceu para registro de entrada:(S/N) ")
             
             if naoapareceu == "N" or naoapareceu == "n":
                removerreserva = input("Deseja remover reserva:(S/N)")
             else:
                print("Retornando para o Menu......")

             if removerreserva == "S" or removerreserva == "s":
                 print("Removendo reserva.........")
                 quarto102 = "disponível"
             else:
                alteradataentrada = input("Deseja mudar a data de entrada:(S/N) ")
                alteradatasaida = input("Deseja mudar a data de saida:(S/N)")
             
             if alteradataentrada == "S" or alteradataentrada == "s" and alteradatasaida == "S" or alteradatasaida == "s":
                dataentrada2 = input("Para quando deseja alterar a data de entrada: ")
                datasaida2 = input("Para quando deseja alterar a data de saida: ")
             else:
                print("Retornando ao menu......")

           if quarto103 == "reservado":
             naoapareceu = input("Hospede apareceu para registro de entrada:(S/N) ")
             
             if naoapareceu == "N" or naoapareceu == "n":
                removerreserva = input("Deseja remover reserva:(S/N)")
             else:
                print("Retornando para o Menu......")

             if removerreserva == "S" or removerreserva == "s":
                 print("Removendo reserva.........")
                 quarto103 = "disponível"
             else:
                alteradataentrada = input("Deseja mudar a data de entrada:(S/N) ")
                alteradatasaida = input("Deseja mudar a data de saida:(S/N)")
             
             if alteradataentrada == "S" or alteradataentrada == "s" and alteradatasaida == "S" or alteradatasaida == "s":
                dataentrada2 = input("Para quando deseja alterar a data de entrada: ")
                datasaida2 = input("Para quando deseja alterar a data de saida: ")
             else:
                print("Retornando ao menu......")

           if quarto104 == "reservado":
             naoapareceu = input("Hospede apareceu para registro de entrada:(S/N) ")
             
             if naoapareceu == "N" or naoapareceu == "n":
                removerreserva = input("Deseja remover reserva:(S/N)")
             else:
                print("Retornando para o Menu......")

             if removerreserva == "S" or removerreserva == "s":
                 print("Removendo reserva.........")
                 quarto104 = "disponível"
             else:
                alteradataentrada = input("Deseja mudar a data de entrada:(S/N) ")
                alteradatasaida = input("Deseja mudar a data de saida:(S/N)")
             
             if alteradataentrada == "S" or alteradataentrada == "s" and alteradatasaida == "S" or alteradatasaida == "s":
                dataentrada2 = input("Para quando deseja alterar a data de entrada: ")
                datasaida2 = input("Para quando deseja alterar a data de saida: ")
             else:
                print("Retornando ao menu......")

           if quarto105 == "reservado":
             naoapareceu = input("Hospede apareceu para registro de entrada:(S/N) ")
             
             if naoapareceu == "N" or naoapareceu == "n":
                removerreserva = input("Deseja remover reserva:(S/N)")
             else:
                print("Retornando para o Menu......")

             if removerreserva == "S" or removerreserva == "s":
                 print("Removendo reserva.........")
                 quarto105 = "disponível"
             else:
                alteradataentrada = input("Deseja mudar a data de entrada:(S/N) ")
                alteradatasaida = input("Deseja mudar a data de saida:(S/N)")
             
             if alteradataentrada == "S" or alteradataentrada == "s" and alteradatasaida == "S" or alteradatasaida == "s":
                dataentrada2 = input("Para quando deseja alterar a data de entrada: ")
                datasaida2 = input("Para quando deseja alterar a data de saida: ")
             else:
                print("Retornando ao menu......")
        case 7:
            #Finalização do programa.    
            print("Finalizando..........")

            break

