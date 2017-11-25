import requests
from time import gmtime, strftime

chce_kupic_BTC = 0.15
print("chce kupic: " + str(chce_kupic_BTC) + " BTC")
print("------------------------------------")

api_btcpln = requests.get("https://bitbay.net/API/Public/BTCPLN/orderbook.json")
btcpln = api_btcpln.json()
ask_btcpln = btcpln["asks"][0:15]
bid_btcpln = btcpln["bids"][0:15]

kurs_ask = []
ilosc_ask = []
suma_ask = []
narast_ask = []
narast_btc = []

for x in range(0, 15):
    kurs_ask.append(ask_btcpln[x][0])
    ilosc_ask.append(ask_btcpln[x][1])
    suma_ask.append(round((ask_btcpln[x][1] * ask_btcpln[x][0]), 1))
    narast_ask.append(0)
    narast_btc.append(0)

narast_ask[0] = suma_ask[0]
narast_btc[0] = ilosc_ask[0]
rekurencja = -1
ile_kupie = 0
ile_wydam = 0

for y in range(0, 15):
    narast_ask[y] = round((narast_ask[y-1] + ask_btcpln[y][1] * ask_btcpln[y][0]), 1)

for y in range(1, 15):
    narast_btc[y] = round((narast_btc[y-1] + ilosc_ask[y]), 8)


#---------------------------------
# ----- szybka transakcja: -------
#---------------------------------

for y in range(0, 15):
    rekurencja += 1
    if narast_btc[y]>chce_kupic_BTC:
        #print ("rekurencja PLN nr: " + str(rekurencja))
        break

ile_kupie = narast_btc[rekurencja]
if ile_kupie > chce_kupic_BTC:
    roznica = ile_kupie - chce_kupic_BTC
#print("roznica wyniesie: " + str("%.8f" % roznica) + " BTC")
#print("ile kupie: " + str(chce_kupic_BTC) + " BTC")

for i in range(0, rekurencja+1):
    ile_wydam += suma_ask[i]
#print("suma PLN: " + str("%.2f" % ile_wydam))
ile_wydam = ile_wydam - (roznica * kurs_ask[rekurencja])
print("ile wydam PLN: " + str("%.2f" % ile_wydam))
sredni_kurs = ile_wydam / chce_kupic_BTC
print("sredni kurs PLN: " + str("%.2f" % sredni_kurs))
print("------------------------------------")

#--------------------------------------
# --- koniec szybkiej transakcji ------
#--------------------------------------



# BTC USD

api_btcUSD = requests.get("https://bitbay.net/API/Public/BTCUSD/orderbook.json")
btcUSD = api_btcUSD.json()
ask_btcUSD = btcUSD["asks"][0:15]
bid_btcUSD = btcUSD["bids"][0:15]

kurs_askUSD = []
ilosc_askUSD = []
suma_askUSD = []
narast_askUSD = []
narast_btcUSD = []

for x in range(0, 15):
    kurs_askUSD.append(ask_btcUSD[x][0])
    ilosc_askUSD.append(ask_btcUSD[x][1])
    suma_askUSD.append(round((ask_btcUSD[x][1] * ask_btcUSD[x][0]), 1))
    narast_askUSD.append(0)
    narast_btcUSD.append(0)

narast_askUSD[0] = suma_askUSD[0]
narast_btcUSD[0] = ilosc_askUSD[0]
rekurencjaUSD = -1
ile_kupieUSD = 0
ile_wydamUSD = 0

for y in range(0, 15):
    narast_askUSD[y] = round((narast_askUSD[y-1] + ask_btcUSD[y][1] * ask_btcUSD[y][0]), 1)

for y in range(1, 15):
    narast_btcUSD[y] = round((narast_btcUSD[y-1] + ilosc_askUSD[y]), 8)


#---------------------------------
# ----- szybka transakcja: -------
#---------------------------------

for y in range(0, 15):
    rekurencjaUSD += 1
    if narast_btcUSD[y]>chce_kupic_BTC:
        #print ("rekurencja USD nr: " + str(rekurencjaUSD))
        break

ile_kupieUSD = narast_btcUSD[rekurencjaUSD]
if ile_kupieUSD > chce_kupic_BTC:
    roznicaUSD = ile_kupieUSD - chce_kupic_BTC
#print("roznica wyniesie: " + str("%.8f" % roznicaUSD) + " BTC")
#print("ile kupie: " + str(chce_kupic_BTC) + " BTC")

for i in range(0, rekurencjaUSD+1):
    ile_wydamUSD += suma_askUSD[i]
#print("suma USD: " + str("%.2f" % ile_wydamUSD))
ile_wydamUSD = ile_wydamUSD - (roznicaUSD * kurs_askUSD[rekurencjaUSD])
print("ile wydam USD: " + str("%.2f" % ile_wydamUSD))
sredni_kursUSD = ile_wydamUSD / chce_kupic_BTC
print("sredni kurs USD: " + str("%.2f" % sredni_kursUSD))
sr_kurs_usdpln = sredni_kursUSD * 3.65
print("sredni kurs (PLN): " + str("%.2f" % sr_kurs_usdpln))

#--------------------------------------
# --- koniec szybkiej transakcji ------
#--------------------------------------

print("------------------------------------")

kurs_dolara = 3.65
ilewydamusdpln = ile_wydamUSD * kurs_dolara

print("kupno za PLN: " + str("%.2f" % ile_wydam) + " PLN")
print("kupno za USD: " + str("%.2f" % ilewydamusdpln) + " PLN")

print("------------------------------------")

procent = 100 * (ilewydamusdpln - ile_wydam) / ilewydamusdpln

print("roznica w zakupie: " + str("%.2f" % procent) + "%")
print("------------------------------------")
print(" . ")
print("------------------------------------")

#drukowanie wyniku do pliku bitbay.txt
f = open("bitbay.txt", mode="a")
f.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
f.write(strftime("%c >> "))
f.write("PLN: " + str("%.2f" % ile_wydam) + " PLN ")
f.write(" |||  USD: " + str("%.2f" % ilewydamusdpln) + " PLN ")
f.write(" |||  roznica w zakupie: " + str("%.2f" % procent) + "% \n")
f.close
