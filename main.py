import requests, bs4
from datetime import datetime

site = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/1336/toledo-pr")

page=bs4.BeautifulSoup(site.text ,"html.parser")
selectMin = page.select("#min-temp-1")
selectMax = page.select("#max-temp-1")
selectTeste = page.select(".highcharts-halo highcharts-color-undefined")

valorMin = selectMin[0].getText()
valorMax = selectMax[0].getText()
valores= [valorMin, valorMax]

dataHoraAtual = datetime.now()
horas = dataHoraAtual.strftime("%H:%M")
dataAtual = dataHoraAtual.strftime("%d/%m/%y")

with open("Clima-Toledo-PR..csv", "w") as arquivo:
    arquivo.write("Hora;Data;Temp Min;Temp Max\n")

    arquivo.write(horas + ";")
    arquivo.write(dataAtual + ";")

    for valor in valorMin:
        arquivo.write(str(valor))
    arquivo.write(";")
    for valor in valorMax:
        arquivo.write(str(valor))
