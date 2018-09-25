import json, csv
from yahoofinancials import YahooFinancials



def make_csv_with_ticker_data(ticker):
    yahoo_financials = YahooFinancials(ticker) #выбраны котировки 
    day_ago = '2018-09-25'
    js_array = yahoo_financials.get_historical_price_data('1900-01-02', day_ago, 'daily') #выбираем всю историю
    prices_array = js_array[ticker]["prices"]

    with open (ticker + '.csv', 'w', encoding = 'utf-8', newline = '') as file_data:
        fields = ["formatted_date", "open", "close"]
        writer = csv.DictWriter(file_data, fields, delimiter=';',extrasaction='ignore')
        writer.writeheader()
        for price_str in prices_array:
            pass
            writer.writerow(price_str)

ticker = input('Введите тикер: ')
make_csv_with_ticker_data(ticker)
