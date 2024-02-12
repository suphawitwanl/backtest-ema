import ccxt
import datetime

# Create an exchange instance
exchange = ccxt.binance()

# Define the trading pair and timeframe
pair = 'BTC/USDT'
timeframe = '15m'

date_list = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']
year_list = ['2020','2021','2022','2023']
# Define the time range
for i in year_list:
    for j in month_list:
        for k in date_list:
            print(f'{i}-{j}-{k}')
            since = exchange.parse8601(f'{i}-{j}-{k}T00:00:00Z')

            # Fetch the OHLCV data
            ohlcv = exchange.fetch_ohlcv(pair, timeframe, since)

            # Convert timestamp to readable date and print the data
            file = open('raw_btc_data02.csv', 'a')
            count = 0
            for candle in ohlcv:

                file.write(f"{datetime.datetime.utcfromtimestamp(ohlcv[count][0] / 1000)},{ohlcv[count][1]},{ohlcv[count][2]},{ohlcv[count][3]},{ohlcv[count][4]},{ohlcv[count][5]}\n")
                count += 1

                """  timestamp = candle[0]
                date = datetime.datetime.utcfromtimestamp(timestamp / 1000)
                print(date, candle[1:]) """

            file.close()
print("Done Done Done")