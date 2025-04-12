import requests
import random
import time

def simular_aproximacao(mac_beacon, distancia):
    """
    Função para simular a aproximação a um beacon, com base no MAC e na distância (simulada).
    """
    url = f"http://127.0.0.1:8000/api/beacons/{mac_beacon}"

    if distancia < 5:
        mensagem = "Você está muito próximo do beacon!"
    elif distancia < 10:
        mensagem = "Aproximando-se do beacon."
    else:
        mensagem = "Você está distante do beacon."

    # Disparar uma requisição GET para obter o beacon e enviar o alerta
    response = requests.get(url)
    if response.status_code == 200:
        beacon_data = response.json()
        print(f"Beacon encontrado: {beacon_data['nome']}")
        print(f"Mensagem: {beacon_data['mensagem']}")
        print(f"Alerta gerado: {mensagem}")
    else:
        print(f"Beacon com MAC {mac_beacon} não encontrado.")

# Testar a simulação com beacons conhecidos
beacons_simulados = [
    {"mac": "FB:5B:92:AE:31:E7", "distancia": random.uniform(1, 20)},  # Beacon da calçada
    {"mac": "EC:48:49:05:5E:5E", "distancia": random.uniform(1, 20)}   # Beacon da esquina
]

for beacon in beacons_simulados:
    simular_aproximacao(beacon["mac"], beacon["distancia"])
    time.sleep(1)
