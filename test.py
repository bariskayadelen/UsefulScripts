import get_currency_tr as cur

# Check web page https status
print(cur.req.status_code)
# 200

# Get bank name
print(cur.company)
# Türkiye İş Bankası

# Get bank url
print(cur.url)
# https://www.isbank.com.tr/en/foreign-exchange-rates

# Get currency code, buy and sell rate
print(cur.price('EUR'))
# ('EUR', 18.1227, 18.9667)