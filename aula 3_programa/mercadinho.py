# autor: Pablo Fernandes
# version: 1.0.1
# date: april/09/2022
# description: este programa cadastra usuario 
# name: mercadinho FATEC

from email import message
from hashlib import sha256
from itertools import count
import sys
from time import sleep

mensagem =  "Olá seja bem-vindo ao Mercadinho FATEC"

for letra in mensagem:
    sys.stdout.write(letra)
    sys.stdout.flush()
    sleep(0.1)
print()
    
opcoes_de_menu = ["sign in", "sign up", "fale conosco"]

count = 1
for opcao in opcoes_de_menu:
    print(f"{count} - {opcao}")
    count += 1


opcao_digitada = input("qual opção deseja? ")

with open("./mercadinho.csv") as arquivo:
    print(arquivo.read())