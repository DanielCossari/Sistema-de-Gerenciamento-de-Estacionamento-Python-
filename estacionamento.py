# SISTEMA DE ESTACIONAMENTO
vagas_totais = 3 #Número máximo de vagas no estacionamento
estacionamento = {} #Armazena veículos atualmente estacionados
historico = [] #Guarda registros de veículos que já sairam
total_arrecadado = 0 #Soma total arrecadado no dia 

#Loop principal
while True:
    print("========== ESTACIONAMENTO ==========")
    print("1 - Entrada de veículo")
    print("2 - Saída de veículo")
    print("3 - Listar veículos estacionados")
    print("4 - Consultar vagas disponíveis")
    print("5 - Histórico de veículos")
    print("6 - Relatório do dia")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    
    # ENTRADA DE VEÍCULO
    if opcao == "1":
        #Verifica se ainda há vagas disponíveis
        if len(estacionamento) < vagas_totais:
            
            #Garante que a placa não seja duplicada
            while True:
                placa = input("Digite a placa: ")
                if placa in estacionamento:
                    print("Esse veículo já está estacionado!")
                else:
                    break
            
            #Coleta de dados do veículo
            nome = input("Nome do proprietário: ")
            modelo = input("Modelo do veículo: ")
            print("Tipo de veículo:")
            print("1 - Carro (R$5/hora)")
            print("2 - Moto (R$3/hora)")
            
            tipo = input("Escolha: ")

            if tipo == "1":
                tipo_veiculo = "Carro"
                valor_hora = 5
            elif tipo == "2":
                tipo_veiculo = "Moto"
                valor_hora = 3
            else:
                print("Tipo inválido!")
                continue #Volta ao menu principal

            #Validação da hora de Entrada
            while True:
                try:
                    entrada = int(input("Hora de entrada (0 a 22): "))
                    if 0 <= entrada <= 22:
                        break
                    else:
                        print("Hora inválida! Digite entre 0 e 22.")
                except:
                        print("Digite um número válido!")
            
            #Armazena o veículo no estacionamento
            estacionamento[placa] = {
                "nome": nome,
                "modelo": modelo,
                "tipo": tipo_veiculo,
                "valor_hora": valor_hora,
                "entrada": entrada
            }

            print("Veículo estacionado com sucesso!")

        else:
            print("Estacionamento lotado!")

    
    # SAÍDA DE VEÍCULO
    elif opcao == "2":
        placa = input("Digite a placa do veículo: ")
        
        #Verifica se o veículo existe
        if placa in estacionamento:
            
            #Validação da hora da Saída
            while True:
                try:
                    saida = int(input("Hora de saída (1 a 23): "))
                    if 0 <= saida <= 23:
                        if saida < entrada:
                            print("Saída não pode ser menor que a entrada!")
                        else:
                            break
                    else:
                        print("Hora inválida!")
                except:
                    print("Digite um número válido!")
            
            #Calcula tempo e valor
            dados = estacionamento[placa]
            entrada = dados["entrada"]
            tempo = saida - entrada

            valor = tempo * dados["valor_hora"]

            print("Tempo estacionado: ",tempo,"horas")
            print(f"Valor a pagar: R$", valor)
            
            #Escolha da forma de pagamento
            print("Forma de pagamento:")
            print("1 - PIX")
            print("2 - Cartão")
            print("3 - Dinheiro")

            pagamento = int(input("Escolha: "))

            if pagamento == 1:
                forma_pagamento = "PIX"
            elif pagamento == 2:
                forma_pagamento = "Cartão"
            elif pagamento == 3:
                forma_pagamento = "Dinheiro"
            else:
                forma_pagamento = "Não informado"

            total_arrecadado += valor #Atualiza o total arrecadado
            
            #registra no histórico
            historico.append({
                "placa": placa,
                "nome": dados["nome"],
                "modelo": dados["modelo"],
                "tipo": dados["tipo"],
                "entrada": entrada,
                "saida": saida,
                "valor": valor,
                "pagamento": forma_pagamento
            })

            del estacionamento[placa] #remove veículo estacionado

            print("Veículo removido com sucesso!")

        else:
            print("Veículo não encontrado!")

  
    # LISTAR VEÍCULOS
    elif opcao == "3":
        if estacionamento:
            print("======= VEÍCULOS ESTACIONADOS =======")
            
            #Percorre todos os veículos estacionados
            for placa, dados in estacionamento.items():
                print(f"Placa: {placa}")
                print(f"Proprietário: {dados['nome']}")
                print(f"Modelo: {dados['modelo']}")
                print(f"Tipo: {dados['tipo']}")
                print(f"Entrada: {dados['entrada']}h")

        else:
            print("Nenhum veículo estacionado.")


    # CONSULTAR VAGAS
    elif opcao == "4":
        vagas_disponiveis = vagas_totais - len(estacionamento)
        print(f"Vagas disponíveis: {vagas_disponiveis}")

   
    # HISTÓRICO
    elif opcao == "5":
        if historico:
            print("========== HISTÓRICO ==========")
            
            #Exibe todos os registros finalizados
            for item in historico:
                print(f"\nPlaca: {item['placa']}")
                print(f"Cliente: {item['nome']}")
                print(f"Modelo: {item['modelo']}")
                print(f"Tipo: {item['tipo']}")
                print(f"Entrada: {item['entrada']}h")
                print(f"Saída: {item['saida']}h")
                print(f"Valor pago: R$ {item['valor']}")
                print(f"Pagamento: {item['pagamento']}")
                print("-" * 30)

        else:
            print("Nenhum histórico registrado.")

   
    # RELATÓRIO DO DIA
    elif opcao == "6":
        print("========== RELATÓRIO DO DIA ==========")
        print(f"Total de veículos atendidos: {len(historico)}")
        print(f"Veículos atualmente estacionados: {len(estacionamento)}")
        print(f"Vagas livres: {vagas_totais - len(estacionamento)}")
        print(f"Total arrecadado: R${total_arrecadado}")

  
    # SAIR
    elif opcao == "7":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
