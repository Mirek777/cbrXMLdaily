import urllib.request
from xml.dom import minidom

webFile = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
data = webFile.read()

with open("test.xml", "wb") as localFile:
    localFile.write(data)

webFile.close()

# Парсинг xml и запись данных в файл
doc = minidom.parse("test.xml")

root = doc.getElementsByTagName("ValCurs")[0]
currency = doc.getElementsByTagName("Valute")

for rate in currency:
    # Венгерский форинт
    if (rate.getAttribute('ID') == 'R01135'):
        venForValue = rate.getElementsByTagName("Value")[0]
        venForValueStr = venForValue.firstChild.data
        venForValueFloat = float(venForValueStr.replace(',', '.', 1) )
        venForN = rate.getElementsByTagName("Name")[0]
        vanForName = venForN.firstChild.data
        print('стоимость', vanForName, 'составит', venForValueFloat, 'руб.')
    # Норвежская крона
    if (rate.getAttribute('ID') == 'R01535'):
        norKronVal = rate.getElementsByTagName("Value")[0]
        norKronValueStr = norKronVal.firstChild.data
        norKronValueFloat = float(norKronValueStr.replace(',', '.', 1))
        norKronN = rate.getElementsByTagName("Name")[0]
        norKronName = norKronN.firstChild.data
        print('стоимость', norKronName, 'составит', norKronValueFloat, 'руб.\n')

# стоимость одной норвежской кроны в венгерских форинтах
print('стоимость одной норвежской кроны составит',
    norKronValueFloat / venForValueFloat, 'венгерских форинтов')
