#receba a entrada de usuario, se ele enviar texto, digite "nao recebemos numero"

entrada_do_usuario = input("digite uma frase ")


if entrada_do_usuario.isalpha():
    print("você entendeu a mensagem") 
else:
    print("não aceitamos número")
    
   