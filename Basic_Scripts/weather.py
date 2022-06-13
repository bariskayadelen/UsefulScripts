import urllib.request
from bs4 import BeautifulSoup as soup

my_url = 'https://weather.com/weather/today/l/6f03ddf87585ae5600e3dee28e519d788ddeb749efefa3f236796ef7167fc411'
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
uClient = urllib.request.urlopen(req)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
# read_time = page_soup.find_all('div', {"class":"CurrentConditions--header--27uOE"})[0].span.text
location = page_soup.find_all('div', {"class":"CurrentConditions--header--27uOE"})[0].find('h1', {"class":"CurrentConditions--location--kyTeL"}).text
temp = page_soup.find_all('div', {"class":"CurrentConditions--primary--2SVPh"})[0].span.text

# print(read_time)
print(location)
print(temp)