# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
#    問題設定:
# 

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# sample_number個の時系列データを生成し、株価の評価をする
sample_number = 100000

# %%
# 株価の日次時系列データ
pd_data = pd.read_csv('sample_data.csv',header=None)
raw_data= np.array(pd_data[0])

# %%
log_data = np.log(raw_data)
# (逆向きの/時間を遡る)日次収益率
sample_rate= -(log_data[1:len(log_data)]-log_data[0:len(log_data)-1])

# %%
price = np.ones(sample_number)*raw_data[len(raw_data)-1]

# sample_number個の株価データの平均値
price_avg = [price[0]]
# sample_number個の株価データの中間値
price_half = [price[0]]
# Value At Risk - 99%の確率で、株価はこれより高くなる
price_var = [price[0]]
# Average + 1 sigma相当 - 35%の確率で、株価はこれより高くなる
price_p = [price[0]]
# Average - 1 sigma相当 - 65%の確率で、株価はこれより高くなる
price_n = [price[0]]

t = len(raw_data)-1
t_list = [t]

for i in range(1,len(raw_data)-1):
    t = t - 1
    t_list.append(t)
    # 変動率をサンプリング
    index = np.random.randint(0,len(sample_rate),sample_number)
    price = (1+sample_rate[index])*price

    price.sort()
    # sample_number個の株価データの平均値
    price_avg.append(np.average(price))
    # sample_number個の株価データの中間値
    price_half.append(price[int(0.5*sample_number)])
    # Value At Risk - 99%の確率で、株価はこれより高くなる
    price_var.append(price[int(0.01*sample_number)])
    # Average + 1 sigma相当 - 35%の確率で、株価はこれより高くなる
    price_n.append(price[int(0.35*sample_number)])
    # Average - 1 sigma相当 - 65%の確率で、株価はこれより高くなる
    price_p.append(price[int(0.65*sample_number)])

plt.plot(raw_data , label="raw data")
plt.plot(t_list, price_avg , label="Average")
plt.plot(t_list, price_half , label= "Half")
plt.plot(t_list, price_var , label= "Value At Risk")
plt.plot(t_list, price_p , label="+1 sigma")
plt.plot(t_list, price_n , label="-1 Sigma")
plt.legend()
plt.show()


# %%



