from random import *
executa = True
adjetivos = [ "maravilhoso" , "acima da média" , " excelente" ]
hobbies = [ "andar de bicicleta" , "programar" , "fazer chá" ]
print("Gerador de Cumprimentos")
print("----------------------")
nome = input("Qual é o seu nome: ")
print('''
Menu
   c = obter cumprimento
   a = adicionar hobby
   d = remover hobby
   p = imprimir hobbies
   q = sair
''')
while executa == True:
    menuChoice = input("\n>_").lower()
    if menuChoice == 'c':
        print("Aqui está o seu cumprimento" , nome, ":")
        print(nome , "você é" , choice(adjetivos) , "em" , choice(hobbies))
        print("De nada!")
    elif menuChoice == 'a':
        itemToadd = input("Adicione o hobby:")
        if itemToadd not in hobbies:
            hobbies.append(itemToadd)
        else:
            print("O hobby já está na lista!")
    elif menuChoice == 'd':
        itemToDelete = input("Insira o hobby a ser removido:")
        if  itemToDelete in hobbies:
            hobbies.remove(itemToDelete)
        else:
            print("O hobby não está na lista!")
    elif menuChoice == 'p':
        print(hobbies)
    elif menuChoice == 'q':
        executa = False
    else:
        print("Insira uma opção válida!")
    
