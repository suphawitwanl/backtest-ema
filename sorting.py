import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("btc15m_backtest.csv")

data.sort_values(by='perf', ascending=False, inplace=True)
data = data.reset_index()
print(data.head(5), "\n")

filtered_df = data[(data['slow_ema'] == 12) & (data['fast_ema'] == 26)]
print(filtered_df)


