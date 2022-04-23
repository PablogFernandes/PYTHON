 #usuario vai digitar um texto e você vai verificar se é consoante ou vogal 
 
entrada_user = input("digite uma letra ou uma frase: ")


if entrada_user.lower() == 'a' or  entrada_user.lower == 'e' or entrada_user.lower == 'i' or entrada_user.lower == 'o' or entrada_user.lower == 'u':
    print ("vogal")
else:
    print("consoante")
