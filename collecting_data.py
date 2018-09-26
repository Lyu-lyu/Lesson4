import json, csv
from yahoofinancials import YahooFinancials
from datetime import date, timedelta


def make_csv_with_ticker_data(ticker):
    yahoo_financials = YahooFinancials(ticker) #taking rates by company ticker  
    yesterday = date.today() - timedelta(1)
    day_ago = yesterday.strftime('%Y-%m-%d')
    js_array = yahoo_financials.get_historical_price_data('1900-01-02', day_ago, 'daily') #getting all history data
    prices_array = js_array[ticker]['prices']
    
    with open ('{}.csv'.format(ticker), 'w', encoding = 'utf-8', newline = '') as file_data:
        fields = ['formatted_date', 'open', 'close']
        writer = csv.DictWriter(file_data, fields, delimiter=';',extrasaction='ignore')
        writer.writeheader()
        for price_str in prices_array:
            writer.writerow(price_str)


while True:
    ticker = input('Введите тикер: ').upper()
    try: 
        make_csv_with_ticker_data(ticker)
        print('Файл успешно создан')
        break
    except ValueError:
        print('Введены неверные данные!')

make_csv_with_ticker_data(ticker)