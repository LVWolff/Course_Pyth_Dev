import requests
import json

def val_info(data, val):
    print("Валюта " + val + ' курс: ' + str(data["Valute"][val]['Value']))

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = json.loads(response.text)

val_l = data["Valute"].keys() #список валют

while True:
    val = input('Введите буквенный код валюты (например USD, AUD, KZT и т.д. или Enter для завершения): ').upper()
    if (not val in val_l) and val != '':
        continue
    elif val == '':
        break
    else:
        val_info(data, val)


