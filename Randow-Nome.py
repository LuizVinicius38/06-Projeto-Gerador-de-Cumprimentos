from os import remove
import random
print("Serviço de escolha de nome para animais de estimação!")
nomeAnimaisM = ["Thor", "Zeus", "Floquinho", "Sheik", "Luke", "Apolo", "Jimmy", "Bolota",
"Nick", "Boris", "Charlie", "Eros Theo", "Tobby", "Barth", "Zé",
"Billy", "Pingo", "Scott", "Totó", "Bob", "Duque", "Elvis", "Lorde",
"Fred", "Toddy", "Sushi", "Dexter", "Pingo", "Spike", "Tom", "Brutus",
"Chico", "Simba", "Lupi", "Woody", "Ted", "Zeca", "Logan", "Loki",
"Mike", "Romeu", "Rocky", "Alfredo", "Toby", "Buddy", "Cookie", "Nico",
"Toddy", "Bidu", "Tommy", "Dom", "Max", "Hulk", "Juca", "Negão",
"Dudu", "Snow", "Kiko", "Joe", "Bidu", "Bud", "Bono", "Joaquim",
"Johnny", "Bolt", "Theodoro", "Benjamin", "Marley", "Paçoca", "Otto", "Tony",
"Ozzy", "Bento", "Lion", "Pepe", "Cookie", "Tobias", "Leo", "Sansão",
"Hulk", "Nino", "Ralf", "Pitoco", "Snoopy", "Pipoca", "Barthô", "Tico",
"Jack", "Bartholomeu", "Jake", "Petter", "Bruce", "Beethoven", "Toy", "Ziggy"]

listaNomeUser = []

nomeAnimaisF = ["Mel", "Lili", "Chloé", "Pérola", "Nina", "Lara", "Sol", "Shakira",
"Maggie", "Mia", "Valentina", "Lady", "Luna", "Maya", "Lucy", "Juju",
"Amora", "Lilica", "Bebel", "Kate", "Lola", "Lolla", "Hannah", "Pandora", "Laika",
"Belinha", "Luli", "Marie", "Bolinha", "Julie", "Vicky", "Pucca", "Nala",
"Bela", "Bella", "Amy", "Manu", "Fiona", "Sofia", "Sophia", "Princesa", "Chérie", "Kyra",
"Malu", "Charlotte", "Lisa", "Safira" "Cacau", "Kiara", "Cherry", "Madonna",
"Cristal", "Vida", "Cléo", "Ruby", "Sofie", "Sophie", "Flor", "Bibi", "Candy",
"Cindy", "Kika", "Angel", "Marry Chanel", "Penélope", "Tequila", "Teka",
"Frida", "Millie", "Tiffany", "Pedrita", "Duda", "Pink", "Gucci", "Gaya",
"Lua", "Mila", "Lana", "Anne", "Babi", "Polly", "Nicole", "Miucha",
"Laila", "Melissa", "Eva", "Nutella", "Minnie", "Suzy", "Linda", "Lia",
"Jolie", "Bia", "Brisa", "Anitta", "Jade", "Filó", "Jujuba", "Floquinho",
"Pipoca", "Pitty", "Vitória", "Sara"]

while True: 
    opcao = str(input("Deseja adicionar um nome ou remover ? (A/R) ")).upper()
    sexo = str(input("Escolha o sexo do animal! (M/F) ")).upper()
    if opcao == "A":
        nomeNovo = str(input("Digite o nome do cachorro! "))
        listaNomeUser.append(nomeNovo)
    elif opcao == "R":
        removerNome = str(input("Digite o nome do cachorro! "))
        listaNomeUser.remove(removerNome)
    elif sexo == "M":
        quantAnimal = int(input("Quantos animais você tem ? "))
        n = 0
        while n < quantAnimal:
            nomes = random.choices(nomeAnimaisM)
            listaNomeUser.append(nomes)
            n = n + 1
        print("Você deve chamar seu(s) animal(is) de estimação de {}" .format(listaNomeUser))
    elif sexo == "F":
        quantAnimal = int(input("Quantos animais você tem ? "))
        n = 0
        while n < quantAnimal:
            nomes = random.choices(nomeAnimaisF)
            listaNomeUser.append(nomes)
            n = n + 1
        print("Você deve chamar seu(s) animal(is) de estimação de {}" .format(listaNomeUser))
    #Passar a opção de adicionar ou remover
    elif opcao == "S":
        pass