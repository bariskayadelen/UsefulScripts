# import get_currency_tr as cur

# # Check web page https status
# print(cur.req.status_code)
# # 200

# # Get bank name
# print(cur.company)
# # Türkiye İş Bankası

# # Get bank url
# print(cur.url)
# # https://www.isbank.com.tr/en/foreign-exchange-rates

# # Get currency code, buy and sell rate
# print(cur.price('EUR'))
# # ('EUR', 18.1227, 18.9667)

from datetime import datetime

import json
import requests

now  = datetime.now()
date = now.strftime("%Y-%m-%d")
time = datetime.timestamp(now)

url = f"https://www.isbank.com.tr/_vti_bin/DV.Isbank/PriceAndRate/PriceAndRateService.svc/GetFxRates?Lang=en&fxRateType=IB&date={date}&time={time}"
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = requests.get(url, headers=header)
data = json.loads(req.content)

# print(data)

for item in data['Data']:
    print(item['description'], item["effectiveRateBuy"], item["effectiveRateSell"], item["fxRateBuy"], item["fxRateSell"])