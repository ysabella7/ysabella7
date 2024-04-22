import statistics
import pandas

df = pandas.read_csv('data_list.csv')

online_Amt1 = df['Amt_One']
print(online_Amt1)

online_Amt2 = df['Amt_Two']
print(online_Amt2)

online_Amt3 = df['Amt_Three']
print(online_Amt3)

mean_value =round(statistics.mean(online_Amt1), 2)
print(mean_value)