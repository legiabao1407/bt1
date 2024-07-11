import pandas as pd
print('2. LIỆT KÊ TẤT CẢ MÃ CHỨNG KHOÁN ĐÃ NIÊM YẾT, MÃ CHỨNG KHOÁN THEO TỪNG SÀN GIAO DỊCH (UPCOM, HSX, ...), MÃ CHỨNG KHOÁN THEO NGÀNH HÀNG (ICB):')

transaction_file_path = "vnstock_listing_companies.csv"
transaction_data = pd.read_csv(transaction_file_path)



all_tickers = transaction_data['ticker'].unique()
all_tickers = transaction_data['ticker'].unique()
print("Tất cả mã chứng khoán đã niêm yết:", ', '.join(all_tickers))

if 'exchange' in transaction_data.columns:
    exchanges = transaction_data['exchange'].unique()
    tickers_by_exchange = {exchange: transaction_data[transaction_data['exchange'] == exchange]['ticker'].unique() for exchange in exchanges}

    print("\nMã chứng khoán theo từng sàn giao dịch:")
    for exchange, tickers in tickers_by_exchange.items():
        print('Sàn ',exchange,': ',tickers)
else:
    print("The column 'exchange' does not exist in the csv file.")


if 'industry' in transaction_data.columns:
    industries = transaction_data['industry'].unique()
    tickers_by_industry = {industry: transaction_data[transaction_data['industry'] == industry]['ticker'].unique() for industry in industries}

    print("\nMã chứng khoán theo ngành hàng (industry):")
    for industry, tickers in tickers_by_industry.items():
        print('Ngành hàng ',industry,': ',tickers)
else:
    print("The column 'industry' does not exist in the csv file.")
