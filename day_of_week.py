import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import datetime

dates = []
x = []
y = []

f = open('data/out.txt').readlines()

x = mpl.dates.datestr2num(f)
y = (x % 1) + 2

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y)
ax.yaxis_date()
fig.autofmt_xdate()

ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%m-%d"))
ax.yaxis.set_major_formatter(mpl.dates.DateFormatter("%H:%M"))
print(dir(ax))

# rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
# loc = RRuleLocator(rule)
# ax.xaxis.set_major_locator(loc)


plt.show()

