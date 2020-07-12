import matplotlib.pyplot as plt
import numpy as np
import datetime

dates = []
values = []
i = 0

for line in open('data/out.txt').readlines():
        dt = datetime.datetime.strptime(line.strip(), '%Y-%m-%d %H:%M:%S')
        values.append(i)
        dates.append(dt)
        i += 1

plt.plot_date(dates, values)

plt.gcf().autofmt_xdate()
plt.show()


input()