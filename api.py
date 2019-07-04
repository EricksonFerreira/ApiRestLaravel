import requests
import json
import os

# Request Area
data = requests.get('http://localhost:8000/api/jogador')
binary = data.content
output = json.loads(binary)
# Menu Area
os.system('clear')
def menu():
        print("--> Bem vindo ao apipy 1.0 <--")
        print( "(Menu)")
        print( ">> Use (1) Para ver jogador")
        print( ">> Use (2) Para inserir jogador")
        print( ">> Use (3) Para atualizar jogador")
        print( ">> Use (4) Para deletar jogador")
        print( ">> Use (0) Para Abortar :/")
menu()
valor = input('Resposta :')
if valor == '1':
    os.system('clear')
    x = 0
    print("\n-----Jogadores encontrados-----\n")
    for item in output:
        print('>> Id:',item['id'],'\n>> Nome: ', item['nome'], '\n>> Time :', item['time'], '\n>> Estado origem :', item['estado_origem'], '\n>> País origem :', item['pais_origem'])
        print('=====================================')
elif valor == '2' :
    os.system('clear')
    print(" >> Use (1) Nome do jogador")
    print(" >> Use (2) Time do jogador")
    print(" >> Use (3) Estado do time")
    print(" >> Use (4) País do time")
    nome = input('Digite o nome do jogador: ')
    time = input("Digite o time do jogador: ")
    estado = input("Digite o estado do time: ")
    pais = input("Digite o país de origem: ")
    requests.post('http://localhost:8000/api/jogador/store', data = {'nome':nome, 'time':time, 'estado_origem':estado, 'pais_origem':pais})
elif valor == '3':
    os.system('clear')
    print(" >> Use (1) Nome do jogador")
    print(" >> Use (2) Time do jogador")
    print(" >> Use (3) Estado do time")
    print(" >> Use (4) País do time")
    identifier = input('Digite o ID do jogador que você deseja alterar: ')
    nome = input('Digite o nome do jogador: ')
    time = input("Digite o time do jogador: ")
    estado = input("Digite o estado do time: ")
    pais = input("Digite o país de origem: ")
    requests.put('http://localhost:8000/api/jogador/update/'+ identifier, data = {'nome':nome, 'time':time, 'estado_origem':estado, 'pais_origem':pais})
elif valor == '4':
    os.system('clear')
    print(" >> Use (1) Deletar apenas um jogador")
    print(" >> Use (2) Para deletar todos os jogadores")
    print(" >> Use (0) Para retornar o menu")
    resposta = input("Resposta :")
    if resposta == '1':
        jogadorId = input('Digite o Id do jogador :')
        requests.delete('http://localhost:8000/api/jogador/destroy/' + jogadorId)
    elif resposta == '2':
        requests.delete('http://localhost:8000/api/jogador/deleteAll/')
    else :
        Menu()
else :
    print("By by :)")
#Percorrendo dados

#Percorrendo dado