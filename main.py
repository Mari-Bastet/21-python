import requests
import json
def comprarCarta(v_deck_id):
    v_comprar_carta = json.loads(requests.get(f"https://deckofcardsapi.com/api/deck/{v_deck_id}/draw/?count=1").content)
    v_carta_comprada = v_comprar_carta["cards"][0]["value"]

    dicionario = {
        "KING": "12",
        "QUEEN": "13",
        "ACE": "11",
        "JACK": "0"}

    v_carta_comprada = int(dicionario.get(v_carta_comprada,v_carta_comprada)) #,v_carta_comprada
    return(v_carta_comprada)

v_deck = json.loads(requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").content)
v_deck_id = v_deck["deck_id"]

distribuir_carta = 0

for i in range(2):
    distribuir_carta += comprarCarta(v_deck_id)

comprar_carta = "S"

while comprar_carta == "S":
    comprar_carta = str(input("Deseja comprar mais alguma carta? (S/N) "))
    if comprar_carta:
        distribuir_carta += comprarCarta(v_deck_id)
    else:
        break

if distribuir_carta > 21:
    print(f"Estourou! {distribuir_carta}")
elif distribuir_carta == 21:
    print(f"Você ganhou! {distribuir_carta}")
else:
    print(f"Chegou perto! {distribuir_carta}")