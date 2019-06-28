import requests
# r = requests.get('http://localhost:8000/api/jogador/')
# r = requests.get('http://localhost:8000/api/jogador/show/1')
# r = requests.post('http://localhost:8000/api/jogador/store/?nome=Riquelme&time=Vitoria&estado_origem=Pernambuco&pais_origem=Brasil')
# r = requests.put('http://localhost:8000/api/jogador/update/1?nome=Paulo&time=Ceara&estado_origem=Bahia&pais_origem=Brasil')
# r = requests.delete('http://localhost:8000/api/jogador/destroy/1')

# r = requests.get('http://localhost:8000/api/times/')
# r = requests.get('http://localhost:8000/api/times/show/1')
r = requests.post('http://localhost:8000/api/times/store/?nome=Flamengo&time=Paulo&estado_origem=Rio de Janeiro&pais_origem=Serie A')
# r = requests.put('http://localhost:8000/api/times/update/1?nome=Paulo&time=Ceara&estado_origem=Bahia&pais_origem=Brasil')
# r = requests.delete('http://localhost:8000/api/times/destroy/1')
print (r.text)