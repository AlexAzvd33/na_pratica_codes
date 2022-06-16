"""

import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()


def getdata(url):
     r = requests.get(url)
     return r.text


htmldata = getdata("https://www.tempo.com/florianopolis.html")

soup = BeautifulSoup(htmldata, 'html.parser')

print(soup.prettify())

current_temp = soup.find_all("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")

chances_rain = soup.find_all("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp = (str(current_temp))

temp_rain = str(chances_rain)


result = "Temperatura agora " + temp[128:-9] + " em Florianópolis" + "\n" + temp_rain[100:-14]
n.show_toast("live Weather update",
             result, duration=10)

"""

import requests

# link do open_weather: https://openweathermap.org/


API_KEY = "*******************" # chave confidencial sua do site;
cidade = "florianopolis"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()

descricao = requisicao_dic['weather'][0]['description']

temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f"{temperatura}ºC")
