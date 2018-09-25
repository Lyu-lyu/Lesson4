import json, csv
from yahoofinancials import YahooFinancials

yahoo_financials = YahooFinancials('MCD') #выбраны котировки McDonald's
js_array = yahoo_financials.get_historical_price_data('1970-01-02', '2018-09-25', 'daily') #выбираем всю историю


