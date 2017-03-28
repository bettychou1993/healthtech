import numpy as np
import json, urllib
import requests
import matplotlib.pyplot as plt
from pylab import *

with open('/Users/bettychou/Desktop/LocationHistory.json') as data_file:    
    data = json.load(data_file)

data['locations'][4]['activitys'][0]['activities'][0]['type']

ms = data['locations'][4]['activitys'][0]['timestampMs']
sec = float(ms)/1000.0

recommended_walking_weekly = 2.5 
recommended_running_weekly = 2
recommended_gym = 1.5

minute = sec/60

hour = minute/60

data['locations']

data['locations'][0]['timestampMs']

count = 0
vals= []
for i in range(len(data['locations'])):
    if 'activitys' in data['locations'][i]:
        count += 1
        if vals != []:
            if data['locations'][i]['activitys'][0]['activities'][0]['type'] in vals:
                continue
            else:
                vals.append(data['locations'][i]['activitys'][0]['activities'][0]['type'])
        else:
            vals.append(data['locations'][i]['activitys'][0]['activities'][0]['type'])

# physical status
vals, count

vals_count = dict((val,0) for val in vals)
vals_time = dict((val,0) for val in vals)

vals_count



vals_time

ts = data['locations'][0]['timestampMs']
for i in range(len(data['locations'])):
    if 'activitys' in data['locations'][i]:
        new_ts = data['locations'][i]['activitys'][0]['timestampMs']
        ts_gap = int(new_ts) - int(ts)
        ts = new_ts
        activity = data['locations'][i]['activitys'][0]['activities'][0]['type']
        vals_count[activity] +=1
        vals_time[activity] += ts_gap



vals_time_norm = vals_time.copy()


factor=1.0/sum(vals_time.values())
for k in vals_time:
  vals_time_norm[k] = vals_time[k]*factor

for k in vals_time:
    vals_time[k] = vals_time[k]/1000/-3600

vals_time_norm

vals_time

vals_week_avg = vals_time.copy()

mini = int(data['locations'][0]['timestampMs'])
maxi = int(data['locations'][0]['timestampMs'])
for i in range(len(data['locations'])):
        new_ts = int(data['locations'][i]['timestampMs'])
        if new_ts>maxi:
            maxi = new_ts
        elif new_ts<mini:
            mini = new_ts

mini

maxi

days_count = (maxi-mini)/1000/3600/24

weeks = days_count / 7.0

weeks

for k in vals_week_avg:
    vals_week_avg[k] /= weeks


vals_week_avg


# In[294]:

#a bar chart for the values in vals_week_avg 
descending = []
for y in reversed(sorted(vals_week_avg.values())):
    k = vals_week_avg.keys()[vals_week_avg.values().index(y)]
    descending.append(tuple([k, y]))
    del vals_week_avg[k]

print descending


# In[295]:

status = zip(*descending)[0]
score = zip(*descending)[1]
x_pos = np.arange(len(status)) 


# In[296]:

status


# In[297]:

score


# In[298]:

x_pos


# In[299]:

slope, intercept = np.polyfit(x_pos, score, 1)
trendline = intercept + (slope * x_pos)


# In[321]:

plt.figure(figsize=(20,10))
plt.plot(x_pos, trendline, color='red', linestyle='--')
plt.bar(x_pos, score,align='center')
plt.xticks(x_pos, status) 
plt.ylabel('status Score')
plt.show()


# In[329]:

# make a bar chart compare the onFoot data and the recommended walking weekly
plt.figure(figsize=(20,10))
n_groups = 1
onFoot = score[2]
recommended_walking_weekly = 2.5

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, onFoot, bar_width,
                 alpha=opacity,
                 color='b',
                 label='onFoot')
 
rects2 = plt.bar(index + bar_width, recommended_walking_weekly, bar_width,
                 alpha=opacity,
                 color='g',
                 label='recommended_walking_weekly')

def autolabel(rects):
    for rect in rects:
        height = float(rect.get_height())
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % float(height),
                ha='center', va='bottom')

plt.xlabel('onFoot vs recommended')
plt.ylabel('hours')
plt.title('comparison')
plt.legend()
 
plt.tight_layout()
autolabel(rects1)
autolabel(rects2)
plt.show()


# In[330]:

# make a bar chart compare the onFoot data and the recommended walking weekly
plt.figure(figsize=(20,10))
n_groups = 1
onBike = score[5]
recommended_gym = 1.5

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, onBike, bar_width,
                 alpha=opacity,
                 color='b',
                 label='onBike')
 
rects2 = plt.bar(index + bar_width, recommended_gym, bar_width,
                 alpha=opacity,
                 color='g',
                 label='recommended_gym')

def autolabel(rects):
    for rect in rects:
        height = float(rect.get_height())
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % float(height),
                ha='center', va='bottom')

plt.xlabel('onBike vs recommended_gym')
plt.ylabel('hours')
plt.title('comparison')
plt.legend()
 
plt.tight_layout()
autolabel(rects1)
autolabel(rects2)
plt.show()


# In[303]:

#pie chart graph for the values in vals_time_norm 
vals_time_norm


# In[304]:

descending2 = []
for y in reversed(sorted(vals_time_norm.values())):
    k = vals_time_norm.keys()[vals_time_norm.values().index(y)]
    descending2.append(tuple([k, y]))
    del vals_time_norm[k]

print descending2


# In[305]:

status2 = zip(*descending2)[0]
score2 = zip(*descending2)[1] 


# In[306]:

len(status2)


# In[307]:

new_status = []
for i in range(len(status2)):
    a = str(status2[i])
    new_status.append(a)


# In[308]:

new_status


# In[309]:

score2


# In[310]:

labels = ['still', 'tilting', 'onFoot', 'inVehicle', 'unknown', 'onBicycle', 'exitingVehicle']
colors = ['red', 'green', 'blue', 'gold', 'yellowgreen', 'lightcoral', 'lightskyblue']


# In[311]:

# pie chart 
plt.figure(figsize=(20,10))
plt.pie(score2, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
