import json
import matplotlib.pyplot as plt
import time
import datetime

format_str = '%m/%d/%Y'
ele_dates = []
gas_dates = []

util = open('utilities.json', 'r')
re_util = json.load(util)
util.close()

fig, ax = plt.subplots()
gas_amount = re_util["Gas"][0]["Amount"]
gas_date = re_util["Gas"][0]["Date"]
for i in gas_date:
    gas_dates.append(datetime.datetime.strptime(i,format_str))
ax.plot_date(gas_dates, gas_amount,'-ro',label='Gas Utilities')

ele_amount = re_util["Electric"][0]["Amount"]
ele_date = re_util["Electric"][0]["Date"]
for i in ele_date:
    ele_dates.append(datetime.datetime.strptime(i,format_str))
ax.plot_date(ele_dates, ele_amount,'-go',label='Electric Utilities')

plt.xticks(rotation=45)
legend = ax.legend(loc='upper left',frameon=False, shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#00FFCC')
fig.suptitle('135 Utilities', fontsize=25)
plt.xlabel('Date', fontsize=20)
plt.ylabel('Price', fontsize=20)
fig.savefig('135_Utilities.jpg',bbox_inches="tight")
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()
  
