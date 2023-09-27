from time import sleep #Nesta parte usamos a importação de uma biblioteca, para usar o comando sleep, que permite pausar o bot por alguns segundos

menubolo = { #Aqui nós começamos a usar a lista, para ter um melhor controle do sabores e valores
    1: ("Pudim", 30.00),
    2: ("Cenoura com Chocolate", 32.00),
    3: ("Brigadeiro", 33.00),
    4: ("Coco com Abacaxi", 34.00),
    5: ("Red Velvet", 35.00),
    6: ("Morango com Chantilly", 36.00),
    7: ("Doce de Leite", 37.00),
    8: ("Mousse de Maracujá", 38.00),
    9: ("Limão Siciliano", 38.00),
    10: ("Cheesecake de Morango", 40.00),
    11: ("Chocolate Belga", 40.00),
    12: ("Tiramisu", 41.00),
    13: ("Baunilha com Framboesa", 39.00),
    14: ("Amêndoas e Caramelo", 42.00),
    15: ("Nozes com Creme", 45.00)
}

def diasemana(): #Aqui criamos um comando def, que define uma função, e é chamada mais abaixo
    print("\n[1] - Domingo\n[2] - Segunda\n[3] - Terça\n[4] - Quarta\n[5] - Quinta\n[6] - Sexta\n[7] - Sábado") 
    x = int(input("\nQue dia da semana é hoje?: ")) #Aqui o usuário consegue colocar o dia da semana, para saber se a loja está aberta e está no horário de funcionamento

    if x == 1:
        print("\nInfelizmente nossa loja não abre nos domingos") 
        sleep(2) #Este comando sleep, faz com que o bot descanse por "?" segundos
    elif x == 2:
        print("\nNas Segundas, nossa loja atende das 13:00 até as 17:00")
        sleep(2)
    elif x == 3:
        print("\nNas Terças, nossa loja atende das 13:00 até as 17:00")
        sleep(2)
    elif x == 4:
        print("\nNas Quartas, nossa loja atende das 13:00 até as 17:00")
        sleep(2)
    elif x == 5:
        print("\nNas Quintas, nossa loja atende das 13:00 até as 17:00")
        sleep(2)
    elif x == 6:
        print("\nNas Sextas, nossa loja atende das 13:00 até as 17:00")
        sleep(2)
    elif x == 7:
        print("\nNos Sábados, nossa loja atende das 11:00 até as 15:00")
        sleep(2)
    else:
        print("\nOpção inválida") 
        sleep(2)

def seupedido(): #Aqui criamos outra definição, quem também será puxada com o menu principal
    preçobolo = [] #Aqui nós temos outra lista, para facilitar a verificação 
    preçototal = 0 #Aqui temos a variável que irá calcular o valor total dos pedidos, ela começará em 0

    while True: 
        print("\nEscolha o sabor do bolo (digite 0 para finalizar seu pedido):") 
        for bolo1, (sabor, preço) in menubolo.items(): #Aqui será mostrado na tela todos os sabores das listas lá na parte superior do código, e todos os seus valores também
            print(f"[{bolo1}] - {sabor} - R$ {preço:.2f}") #Puxamos a informação de "menubolo"
        
        escolha = int(input("Digite os sabores desejados: ")) #Aqui o usuário faz a escolha dos sabores 

        if escolha == 0: #Aqui temos uma verificação onde ao digitar 0 o pedido se encerra
            break 
        elif escolha in menubolo: #Aqui, caso a escolha do sabor, esteja dentro dos sabores listados ele continuará o código
            sabor, preço = menubolo[escolha] 
            preçobolo.append(sabor) #Aqui temos o comando append que serve para adicionar um conteúdo a uma lista 
            preçototal += preço #Aqui usamos o sinal de += para somar os valores e mostrar o resultado
            print(f"\nVocê escolheu: {sabor} - R$ {preço:.2f}") #Aqui o comando :.2f é usado para formatar aquela variável, transformando ela em um número com 2 casas decimais apenas
        else:
            print("\nOpção inválida")

    if preçobolo:
        print("\nPedido:")
        for bolo in preçobolo:
            print(bolo)
        print(f"Total a pagar: R$ {preçototal:.2f}") #Aqui será um momento onde será realizado o término do pedido, mostrando o valor a pagar e coletando mais informações sobre entrega
        print("\nNos informe seu endereço: ")
        input("\nBairro: ")
        input("Rua: ")
        input("Número: ")
        input("Complemento: ")
        print("\n Nossa chave pix para realizar o pagamento é: 'Imagine uma chave pix inserida aqui ok'") #Aqui nós colocamos apenas um texto simbolizando uma chave pix 
        sleep(3)
        print("\nAgradecemos por seu pedido, após o pagamento ser efetuado, seu pedido sairá para a entrega. Obrigado pela confiança")
        sleep(3)

def main_menu(): #Aqui nós temos o menu principal, e ele está localizado mais abaixo, porém, inicia primeiro pois todos os comandos estão dentro de um comando "def" e podemos assim, chamá-los quando quisermos.
    while True: 
        print("\n------------------------------------------")
        print("\nOlá, seja bem-vindo(a) a nossa loja Cakes da Gabriela, o que gostaria?")
        print("\n[1] - Fazer pedido\n[2] - Cardápio e valores\n[3] - Saber mais sobre a empresa\n[4] - Status da loja\n[0] - Sair") 
        x = int(input("\nDigite a opção desejada: "))

        if x == 0:
            break #Aqui temos a situação onde o usuário já no menu principal, ao digitar 0, encerrará todo o atendimento
        elif x == 1:
            seupedido() #Ao selecionar a opção 1, será iniciado a função "seupedido", desta forma ele puxará os comandos acima e colocará em execução
        elif x == 2:
            print("\nCardápio e valores:")
            for sabor, (nome, preço) in menubolo.items(): #Aqui temos mais uma vez um exemplo de praticidade das listas mostrando exatemente o que queremos na tela
                print(f"{sabor} - {nome} - R$ {preço:.2f}") 
            sleep(5)
        elif x == 3:
            print("\nNós somos a empresa Cakes da Gabriela, temos mais de 5 anos já no mercado vendendo bolos\nAtualmente atendemos na região de Cinelândia e Botafogo\nNosso compromisso é com sua satisfação, realizando sonhos em cada fatia")
            sleep(3)
        elif x == 4:
            diasemana() #Aqui, ao selecionar a opção 4, faremos com que seja colocado em prática a definição "diasemana" onde irá mostrar se a loja está aberta e o horário de atendimento
        else:
            print("\nOpção inválida")
            sleep(2)


main_menu() #Aqui temos o último comando, fazendo a estrutura de repetição, onde ao finalizar cada processo, o atendimento voltará a página inicial para saber se o usuário deseja mais alguma coisa, ou, ao apertar 0 já no menu principal, encerrar o atendimento
