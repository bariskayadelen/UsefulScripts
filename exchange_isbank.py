from datetime import datetime
import json
import requests

date = str(datetime.today().strftime('%Y-%m-%d'))
time = str(datetime.today().strftime("%H:%M:%S"))

url = f"https://www.isbank.com.tr/_vti_bin/DV.Isbank/PriceAndRate/PriceAndRateService.svc/GetFxRates?Lang=tr&fxRateType=IB&date={date}&time={time}"
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'}

req = requests.get(url, headers=header)
data = json.loads(req.content)

for item in data['Data']:
    # print(item['code'], item['description'], item["effectiveRateBuy"], item["effectiveRateSell"], item["fxRateBuy"], item["fxRateSell"])
    print(item['code'], item["effectiveRateBuy"], item["effectiveRateSell"])

currency_list = {'USD':'0', 'EUR':'1', 'GBP':'2', 'AUD':'4', 'DKK':'5', 'SEK':'6', 'CHF':'7', 'JPY':'8', 'CAD':'9', 'KWD':'10', 'NOK':'11', 'SAR':'12', 'XAU':'3'}

def currency(code):
    x = int(currency_list[code])
    # currency_code = data['Data'][x]['code']
    buy = data['Data'][x]['effectiveRateBuy']
    sell = data['Data'][x]['effectiveRateSell']
    return buy, sell

exchange_buy = float(currency('XAU')[0])
exchange_sell = float(currency('XAU')[1])

for item in currency_list:
    print

# Main function
def main():
    # Table Width
    tbl_len_out = 74
    tbl_len_in = 24

    # Print Currencies and rates
    print(f"\n{' ISBANK EXCHANGE RATES ':=^{tbl_len_out}}\n")
    print(f"\n{' Döviz':<{tbl_len_in}}   Alış\t\tSatış")
    print(f" {'':-^{tbl_len_in}}  {'':-^{9}}    {'':-^{9}}")

    for item in data['Data']:
        # print(item['code'], item['description'], item["effectiveRateBuy"], item["effectiveRateSell"], item["fxRateBuy"], item["fxRateSell"])
        # print(item['code'], item["effectiveRateBuy"], item["effectiveRateSell"])
        print(f"{item['code']:^{tbl_len_in}} : {item['effectiveRateBuy']:^{9}}   {item['effectiveRateSell']:^{9}}")

        # print(f"\n{' XAU ':<{tbl_len_in}} :{exchange_buy:^{9}}    {exchange_sell:^{9}}")
#     # print(f"{' City':<{tbl_len_in}} : {fuel_district}")

#     for item in data['Data']:
#         # print(item['code'], item["effectiveRateBuy"], item["effectiveRateSell"])
#         if item['code'] == 'USD':
#             usd_buy = item["effectiveRateBuy"]
#             usd_sell = item["effectiveRateSell"]
#             # return usd_buy, usd_sell
#             print (usd_buy, usd_sell)
    # print(currency_code, currency_buy, currency_sell)
    print(f"\n{'':=^{tbl_len_out}}\n")

if __name__ == "__main__":
    main()