import requests

chce_kupic_waluta1 = float(input("Podaj ile waluty chcesz kupić: "))
print("Chcesz kupić: " + str(chce_kupic_waluta1) + " BTC")

adres_json = "https://bitbay.net/API/Public/BTCPLN/orderbook.json"
kursy = requests.get(adres_json).json()
market_ask = kursy["asks"][0:20]
market_bid = kursy["bids"][0:20]

kurs_ask = []
ilosc_ask = []
cena_ask = []
waluta1_narast_ask = []
waluta2_narast_ask = []

for x in range(0, 20):
    kurs_ask.append(market_ask[x][0])
    ilosc_ask.append(market_ask[x][1])
    cena_ask.append(round((market_ask[x][1] * market_ask[x][0]), 1))
    waluta1_narast_ask.append(0)
    waluta2_narast_ask.append(0)

waluta1_narast_ask[0] = cena_ask[0]
waluta2_narast_ask[0] = ilosc_ask[0]
rekurencja = -1

for y in range(0, 20):
    waluta1_narast_ask[y] = round((waluta1_narast_ask[y-1] + market_ask[y][1] * market_ask[y][0]), 1)

for y in range(1, 20):
    waluta2_narast_ask[y] = round((waluta2_narast_ask[y-1] + ilosc_ask[y]), 8)
    
#---------------------------------
# ----- szybka transakcja: -------
#---------------------------------

for y in range(0, 20):   
    rekurencja += 1     
    if waluta2_narast_ask[y]>chce_kupic_waluta1:
        break

ile_kupie = waluta2_narast_ask[rekurencja]
roznica = ile_kupie - chce_kupic_waluta1

ile_wydam = 0
for i in range(0, rekurencja+1):
    ile_wydam += cena_ask[i]

ile_wydam = ile_wydam - (roznica * kurs_ask[rekurencja])
print("Cena PLN: " + str("%.2f" % ile_wydam))

sredni_kurs = ile_wydam / chce_kupic_waluta1
print("Średni kurs PLN: " + str("%.2f" % sredni_kurs))
