import pandas as pd

data = pd.read_csv("raw_btc_data02.csv")
data = data.drop_duplicates()
data = data.sort_values(by='Date')
data.to_csv("cleaned_btc_15m_02.csv", index=False)
print(data)