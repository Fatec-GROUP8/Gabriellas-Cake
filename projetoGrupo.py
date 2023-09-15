print("-----------------------------------------------------------\n Bem-Vindo(a) a central de dúvidas!!")
 
def startMenu(): 
    print("-----------------------------------------------------------")

    options = ["1 - Bolos", "2 - Tortas", "3 - Doces", "4 - Salgados", "5 - Sair"]
    print("Escolha uma das opções para fazer um pedido:")

    for option in options:
        print(option)

    menuChoice = int(input("Digite o número da opção desejada: "))

    if menuChoice == 1:
        stageOne()
    elif menuChoice == 2:
        stageTwo()
    elif menuChoice == 3:
        stageThree()
    elif menuChoice == 4:
        return
    else:
        startMenu()

def exitMenu(type):
    exit = int(input("[1]Sair\n[2]Retornar\n[3]Retornar ao inicio\n-->"))

    if exit == 1:
        return
    elif exit == 2 and type == "one":
        stageOne()
    elif exit == 2 and type == "two":
        stageTwo()
    elif exit == 2 and type == "three":
        stageThree()
    elif exit == 3:
        startMenu()
    else:
        print("Erro! escolha entre as opções 1, 2 ou 3\n")
        exitMenu(type)

def stageOne():
    print("-----------------------------------------------------------")

    options = ["1 - Link de Acesso?", "2 - Pontuação esperada?", "3 - Quais tecnologias treinar?", "4 - Retornar ao início"]
    print("Escolha uma das opções para fazer um pedido:")

    for option in options:
        print(option)

    answer = int(input("Digite o número da opção desejada: "))

    if answer == 1:
        print("\nhttps://codewars.com\n")
    elif answer == 2:
        print("\nNo codeWars é esperado apenas que você se desafie\n")
    elif answer == 3:
        print("\nCaso você seja iniciante é indicado que use python ou javascript. Porém, o CodeWars possue mais de 30 linguagens disponíveis para você se desafiar.\n")
    elif answer == 4:
        startMenu()
    else:
        print("\nSomente números de 1 a 4 são aceitos!")
        stageOne()
        return
                
    exitMenu("one")

def stageTwo():
    print("-----------------------------------------------------------")

    options = ["1 - O que o Discord faz?", "2 - Link de Acesso?", "3 - Como criar um servidor no Discord?", "4 - Retornar ao início"]
    print("Escolha uma das opções para fazer um pedido:")

    for option in options:
        print(option)

    answer = int(input("Digite o número da opção desejada: "))
        
    if answer == 1:
        print("\nÉ uma plataforma que permiti pessoas com interesses semelhantes compartilharem e se comunicarem, com conversas por voz, vídeo e texto com amigos. Participe de comunidades diversas\n")
    elif answer == 2:
        print("\nhttps://discord.com\n")
    elif answer == 3:
        print("\nAcesse o link a seguir: https://support.discord.com/hc/pt-br/articles/204849977-Como-Criar-um-Servidor-\n")
    elif answer == 4:
        startMenu()
    else:
        print("\nSomente números de 1 a 4 são aceitos!")
        stageTwo()
        return
                
    exitMenu("two")

def stageThree():
    print("-----------------------------------------------------------")

    options = ["1 - Link de Acesso para o Portal Resilia?", "2 - Onde encontro os projetos?", "3 - onde encontro os exercícios?", "4 - Retornar ao início"]
    print("Escolha uma das opções para fazer um pedido:")

    for option in options:
        print(option)

    answer = int(input("Digite o número da opção desejada: "))
         
    print("-----------------------------------------------------------")
    if answer == 1:
        print("\nhttps://aluno.resilia.work\n")
    elif answer == 2:
        print("\nAcesse o portal da resilia, vá em 'Materias da jornada' na esquerda. As propostas de projetos estarão no final do módulo.\n")
    elif answer == 3:
        startMenu()
    else:
        print("\nSomente números de 1 a 3 são aceitos!")
        stageThree()
        return
                
    exitMenu("three")

startMenu()
