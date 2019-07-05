import requests
import json
import os

# Request Area
data = requests.get('http://localhost:8000/api/jogador')
data1 = requests.get('http://localhost:8000/api/times')
binary = data.content
binary1 = data.content
output = json.loads(binary)
output1 = json.loads(binary1)
# Menu Area
os.system('clear')
def menu():
        print("--> Bem vindo ao apipy 1.0 <--")
        print( "(Menu)")
        print( ">> Use (1) Para ver jogador")
        print( ">> Use (2) Para ver times")
        print( ">> Use (3) Para inserir jogador")
        print( ">> Use (4) Para inserir times")
        print( ">> Use (5) Para atualizar jogador")
        print( ">> Use (6) Para atualizar times")
        print( ">> Use (7) Para deletar jogador")
        print( ">> Use (8) Para deletar times")
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
elif valor == '2':
    os.system('clear')
    x = 0
    print("\n-----Times encontrados-----\n")
    for item in output1:
        print('>> Id:',item['id'],'\n>> Nome: ', item['nome'], '\n>> Criador :', item['criador'], '\n>> Estado :', item['estado'], '\n>> Divisão :', item['divisao'])
        print('=====================================')
elif valor == '3' :
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
elif valor == '4' :
    os.system('clear')
    print(" >> Use (1) Nome do time")
    print(" >> Use (2) Criador do time")
    print(" >> Use (3) Estado do time")
    print(" >> Use (4) País do time")
    nome = input('Digite o nome do jogador: ')
    criador = input("Digite o time do jogador: ")
    estado = input("Digite o estado do time: ")
    divisao = input("Digite a divisão do time: ")
    requests.post('http://localhost:8000/api/time/store', data = {'nome':nome, 'criador':criador, 'estado':estado, 'divisao':divisao})
elif valor == '5':
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
elif valor == '6':
    os.system('clear')
    print(" >> Use (1) Nome do time")
    print(" >> Use (2) Criador do time")
    print(" >> Use (3) Estado do time")
    print(" >> Use (4) País do time")
    identifier = input('Digite o ID do jogador que você deseja alterar: ')
    nome = input('Digite o nome do jogador: ')
    criador = input("Digite o time do jogador: ")
    estado = input("Digite o estado do time: ")
    divisao = input("Digite o país de origem: ")
    requests.put('http://localhost:8000/api/time/update/'+ identifier, data = {'nome':nome, 'criador':criador, 'estado':estado, 'divisao':divisao})
elif valor == '7':
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
elif valor == '8':
    os.system('clear')
    print(" >> Use (1) Deletar apenas um time")
    print(" >> Use (2) Para deletar todos os times")
    print(" >> Use (0) Para retornar o menu")
    resposta = input("Resposta :")
    if resposta == '1':
        timeId = input('Digite o Id do time :')
        requests.delete('http://localhost:8000/api/time/destroy/' + timeId)
    elif resposta == '2':
        requests.delete('http://localhost:8000/api/time/deleteAll/')
    else :
        Menu()
else :
    print("Bye Bye")
