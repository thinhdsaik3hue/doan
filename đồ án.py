import pandas as pd
import os
import scipy.stats as stats
df_datas = pd.read_excel(os.path.join("C:/Users/qcth0/PycharmProjects/pythonProject/Temperature.xlsx"))
print(df_datas.loc[1:5, ["Temperature", "Salinity"]])
# Kiểm định t một mẫu (One sample t-test)
print(stats.ttest_1samp(a=df_datas.loc[1:5, ["Temperature", "Salinity"]], popmean=15))
# Kiểm định t hai mẫu (Two sample t-test)
print(stats.ttest_ind(a=df_datas.loc[1:5, ["Temperature"]], b=df_datas.loc[1:5, ["Salinity"]], equal_var=True))

print(stats.ttest_rel(df_datas.loc[1:5, ["Temperature"]], df_datas.loc[1:5, ["Salinity"]]))