# import requests
# from bs4 import BeautifulSoup

# company = "Türkiye Cumhuriyet Merkez Bankası"
# url = "https://www.tcmb.gov.tr/kurlar/today.xml"

# # req = requests.get(url).content.decode("utf-8")
# # print(req)

# xml_data = requests.get(url).content
# soup = BeautifulSoup(xml_data, 'xml')
# print(soup)

# # usd_buy = page_soup.find_all("unit")

# # print(usd_buy)

import requests
import xml.etree.ElementTree as ET

url = 'https://www.tcmb.gov.tr/kurlar/today.xml'
xml_data = requests.get(url).content.decode('utf-8')

tree = ET.fromstring(xml_data)
# root = tree.getroot()

print(tree())

# for child in root.findall:
#     print(child.tag, child.attrib)
