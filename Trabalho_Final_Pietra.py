print("---------Cadastro de clientes----------")

#CADASTRO DE CLIENTE
nome = input("Informe o nome do cliente: ")
telefone = int(input("Informe o telefone do cliente: "))
email = input("Informe o e-mail do cliente: ")
saldo = float(input("Informe o saldo total que o cliente tem disponível: "))

#TABELA DE FIPE DOS VEÍCULOS
tabelafipe = {
    "Civic Type-R": 148929, "City": 71186, "HR-V Turbo": 158855, #Honda
    "Cerato": 91969, "Soul": 85572, "Carnival": 585451, #Kia
    "Eclipse Turbo": 49884, "Lancer Evoution": 58691, "ASX": 69384, #Mitsubish
    "M3": 391974, "320i Turbo": 97650, "X1": 117893, #BMW
    "AMG GT": 1961238, "AMG G63": 2053078, "GT 63S": 1121669 #Mercedes
}

#TABELA DE VEÍCULOS DISPONIVEIS
tabelacarros = {
    "Honda":["Civic Type-R", "City", "HR-V Turbo"],
    "Kia": ["Cerato", "Soul", "Carnival"],
    "Mitsubish": ["Eclipse Turbo", "Lancer Evoution", "ASX"],
    "BMW": ["M3", "320i Turbo", "X1"],
    "Mercedes": ["AMG GT", "AMG G63", "GT 63S"]
}

 #LOOPING DO MENU DE OPÇÕES DE VENDA, COMPRA E LOCAÇÃO DO VEÍCULO
while True:

 opcao = int(input("----------Seja Bem Vindo a Dreams Car, aonde seus sonhos automobilisticos se tornam realidade---------- \n---------------------Menu de Opções----------------- \n1 - Compra de Veículos \n2 - Venda de Veículos \n3 - Locação de Veículos \n4 - Sair \nDigite a opção desejada de acordo com o menu: "))

  #SISTEMA DE VENDA DE VEÍCULO DO CLIENTE
 if opcao == 1:
    print("----------Sistema de Compras de Veículos----------")
      
      #FOR UTILIZADO PARA VERIFICAR SE A MARCA DO VEÍCULO ESTA NA TABELA DE CARROS PARA ENTRAR EM LOOP DO SISTEMA DE COMPRAS
    for marcacarro in tabelacarros:
        print(marcacarro)
    
    marcacarro = input("Escolha uma marca: ")
      #FOR UTILIZADO PARA VERIFICAR SE O MODELO DO VEÍCULO ESTA NA TABELA FIPE PARA CONTINUAR O LOOP DO SISTEMA DE COMPRAR E FAZER O CÁLCULO DO VALOR DO VEÍCULO
    for modelo in tabelafipe:
        print(tabelacarros[marcacarro])
        modelo = input("Escolha um modelo: ")

        descontofipe = tabelafipe[modelo] * 0.12
        proposta = tabelafipe[modelo] - descontofipe

        print(f"\nA proposta para o veículo será de R${proposta:.2f}")
        finalizarproposta = input("Deseja finalizar o negocio de acordo com a proposta (S/N): ").lower()
         
          #IF UTILIZADO PARA CONFIRMAÇÃO DE VENDA DO VEICULO
        if finalizarproposta == "s":
           saldocliente = proposta + saldo

           print(f"Compra realizada com sucesso, saldo disponivel do cliente é R${saldocliente}")
           
          #ELSE UTILIZADO PARA VERIFICAÇÃO DE (NÃO) CONFIRMAÇÃO DE VENDA DO VEÍCULO
        else:
           print("Negocio cancelado")

  #SISTEMA DE VENDA DE VEÍCULO PARA O CLIENTE
 if opcao == 2:
    print("----------Sistema de Vendas de Veículos----------")
      
      #FOR UTILIZADO PARA VERIFICAR SE A MARCA DO VEÍCULO ESTA NA TABELA DE CARROS PARA ENTRAR EM LOOP DO SISTEMA DE VENDA
    for marcacarro in tabelacarros:
        print(marcacarro)
    
    marcacarro = input("Escolha uma marca: ")
     
    print(tabelacarros[marcacarro])
    modelo = input("Escolha um modelo: ")
       
       #IF UTILIZADO PARA VERIFICAÇÃO DA DISPONIBILIDADE DO VEÍCULO PARA CONTINUAR O SISTEMA DE VENDA E FAZER O CÁLCULO DO VALOR DO VEÍCULO
    if modelo in tabelacarros[marcacarro]:
    
        taxafipe = tabelafipe[modelo] * 0.25
        valorvenda = tabelafipe[modelo] + taxafipe

        print(f"O carro desejado {marcacarro} {modelo} no valor de R${valorvenda}")

        finalizarcompra = input("Deseja finalizar compra (S/N): ").lower()
          
          #IF UTILIZADO PARA CONFIRMAÇÃO DE COMPRA DO VEICULO
        if finalizarcompra == "s":
             
             #IF UTILIZADO PARA VERIFICAÇÃO DO SALDO DO CLIENTE
           if saldo < valorvenda:
            print("Saldo insuficiente")
            
            #ELSE UTILIZADO PARA VERIFICAÇÃO DE SALDO (NÃO) SUFICIENTE DO CLIENTE E RETORNA PARA O MENU DE OPÇÕES
           else:
              saldocliente = saldo - valorvenda
              print(f"Venda realizado com sucesso, saldo do cliente é de: R${saldocliente}")
              tabelacarros[marcacarro].remove(modelo)
              
           #ELSE UTILIZIDO PARA VERIFICAÇÃO DE (NÃO) CONFIRMAÇÃO DE COMPRA DO VEÍCULO
        else:
              print("Negóciação cancelada, obrigado por utilizar dos nossos serviços!!!")
      
      #ELSE UTILIZADO PARA VERIFICAÇÃO DA (NÃO) DISPONIBILIDADE DO VEÍCULO E RETORNA PARA O MENU DE OPÇÕES
    else:
       print("Carro já vendido, selecione outro disponível!")
       continue
  
  #SISTEMA DE LOCAÇÃO DE VEÍCULO PAR CLIENTE
 if opcao == 3:
    print("----------Sistema de Locação de Veículos----------")
      
      #FOR UTILIZADO PARA VERIFICAR SE A MARCA DO CARRO ESTA NA TABELA DE CARROS PARA ENTRAR EM LOOP
    for marcacarro in tabelacarros:
        print(marcacarro)
    
    marcacarro = input("Escolha uma marca: ")
     
    print(tabelacarros[marcacarro])
    modelo = input("Escolha um modelo: ")

    diaria = int(input("Insira quantos dias deseja alugar o carro: "))
       #IF UTILIZADO PARA VERIFICAÇÃO DA DISPONIBILIDADE DO VEÍCULO PARA CONTINUAR O SISTEMA DE LOCAÇÃO E FAZER O CÁLCULO DO VALOR DE LOCAÇÃO DO VEÍCULO
    if modelo in tabelacarros[marcacarro]:
    
        valoraluguel = 77 * diaria

        print(f"O carro desejado {marcacarro} {modelo} o valor de locaçãp será de R${valoraluguel}")

        finalizaraluguel = input("Deseja finalizar o pedido para alugar o carro (S/N): ").lower()
          
          #IF UTILIZADO PARA VERIFICAÇÃO DE CONFIRMAÇÃO DE LOCAÇÃO DO VEÍCULO
        if finalizaraluguel == "s":
            
              #IF UTILIZADO PARA VERIFICAÇÃO DO SALDO DO CLIENTE
           if saldo < valoraluguel:
            print("Saldo insuficiente")
  
              #ELSE UTILIZADO PARA VERIFICAÇÃO DE SALDO (NÃO) SUFICIENTE DO CLIENTE E RETORNA PARA O MENU DE OPÇÕES
           else:
              saldocliente = saldo - valoraluguel
              print(f"Carro alugado com sucesso, saldo do cliente é de: R${saldocliente}")
              tabelacarros[marcacarro].remove(modelo)
          
          #ELSE UTILIZIDO PARA VERIFICAÇÃO DE (NÃO) CONFIRMAÇÃO DE LOCAÇÃO DO VEÍCULO
        else:
              print("Negóciação cancelada, obrigado por utilizar dos nossos serviços!!!")
      
      #ELSE UTILIZADO PARA VERIFICAÇÃO DA (NÃO) DISPONIBILIDADE DO VEÍCULO E RETORNA PARA O MENU DE OPÇÕES
    else:
       print("Carro já alugado, selecione outro disponível!")
       continue
 
  #FINALIZAÇÃO DO SISTEMA
 if opcao == 4:
    print("Finalizando sistema, a Dreams Car agradece pela preferencia!!!!")