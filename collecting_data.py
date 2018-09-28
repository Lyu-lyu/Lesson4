import json, csv
from yahoofinancials import YahooFinancials
from datetime import date, timedelta


def make_csv_with_ticker_data(ticker, today):
    yahoo_financials = YahooFinancials(ticker) #taking rates by company ticker  
    js_array = yahoo_financials.get_historical_price_data('1900-01-02', today, 'daily') #getting all history data
    price_array = js_array[ticker]['prices']
    return price_array


def save_to_file(ticker, spreadsheet):
    filename = '{}.csv'.format(ticker)
    with open (filename, 'w', encoding = 'utf-8', newline = '') as file_data:
        fields = ['formatted_date', 'open', 'close']
        writer = csv.DictWriter(file_data, fields, delimiter=';',extrasaction='ignore')
        writer.writeheader()
        for price_str in spreadsheet:
            writer.writerow(price_str)


def main():
    while True:
        ticker = input('Введите тикер: ').upper()
        today = date.today().strftime('%Y-%m-%d')
        try:
            save_to_file(ticker, make_csv_with_ticker_data(ticker, today))
            print('Файл успешно создан')
            break
        except ValueError:
            print('Введены неверные данные!')


if __name__ == '__main__':
    main()