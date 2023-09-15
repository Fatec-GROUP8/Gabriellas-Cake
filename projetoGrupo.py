print("-----------------------------------------------------------\n Bem-Vindo(a) a central de dúvidas!!")
 
def startMenu(): 
    print("-----------------------------------------------------------")

    menuChoice = int(input("\n\
    [1]Dúvidas sobre o CodeWars\n\
    [2]Dúvidas sobre o Discord\n\
    [3]Dúvidas sobre as Aulas \n\
    [4]Sair\n\
    \nEscolha uma das opções: "))

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

    answer = int(input("\n\
    [1]Link de Acesso?\n\
    [2]Pontuação esperada?\n\
    [3]Quais tecnologias treinar?\n\
    [4]Retornar ao início\n\
    \nEscolha uma das opções: "))

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
        
    answer = int(input("\n\
    [1]O que o Discord faz?\n\
    [2]Link de Acesso?\n\
    [3]Como criar um servidor no Discord?\n\
    [4]Retornar ao início\n\
    \nEscolha uma das opções: "))

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
        
    answer = int(input("\n\
    [1]Link de Acesso Portal Resilia?\n\
    [2]Onde encontro os projetos?\n\
    [3]Retornar ao início\n\
    \nEscolha uma das opções: "))


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

