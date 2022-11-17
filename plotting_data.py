# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Austin
#               Christopher
#               Reed
#               Eddy
# Section:      468
# Assignment:   12 - 17 plotting data
# Date:         November 15, 2022

import numpy
import matplotlib.pyplot as plt


readFile = open('WeatherDataCLL.csv', 'r')
days = []
temp_max = []   # -2 index
temp_min = []   # -1 index
rain = []
dates = []
for line in readFile:
    try:
        line = line.rstrip('\n')
        sngl_day = line.split(',')
        temp_min.append(int(sngl_day[-1]))
        temp_max.append(int(sngl_day[-2]))
        rain.append(float(sngl_day[2]))
        days.append(sngl_day)
    except ValueError:
        pass

# x for plot 1
day_num_plt1x = []
for i in range(len(days)):
    day_num_plt1x.append(i)

# y1 for plot 1, max temp
max_temp_plt1y = []
for day in days:
    max_temp_plt1y.append(float(day[-2]))

# y2 for plot 1, wind speed average
avg_windspeed_plt1y = []
for day in days:
    avg_windspeed_plt1y.append(float(day[1]))

fig, left_axis = plt.subplots()
right_axis = left_axis.twinx()

left_axis.set_xlabel('date')

left_axis.plot(day_num_plt1x, max_temp_plt1y, 'r-', label='Max Temp')
left_axis.set_ylabel('Maximum Temperature, F')

right_axis.plot(day_num_plt1x, avg_windspeed_plt1y, 'b-', label='Avg Wind')
right_axis.set_ylabel('Average wind speed, mph')

fig.legend(loc='lower left', bbox_to_anchor=(0.11, 0.13))
plt.title('Maximum Temperature and Average Wind Speed')
plt.tight_layout()
plt.show()

# plot 2
wind_speed_x = []
avg_windspeed = avg_windspeed_plt1y
for x in numpy.linspace(0, 20, 30):
    wind_speed_x.append(x)

days_y_plt2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(wind_speed_x)):
    for windspeed in avg_windspeed:
        try:
            if wind_speed_x[i] <= windspeed <= wind_speed_x[i+1]:
                diff1 = windspeed - wind_speed_x[i]
                diff2 = (windspeed - wind_speed_x[i+1]) * -1
                if diff2 > diff1:
                    days_y_plt2[i+1] += 1
                else:
                    days_y_plt2[i] += 1
        except IndexError:
            pass

plt.bar(wind_speed_x, days_y_plt2, color='g', edgecolor='k', width=20/30)
plt.title('Histogram of average wind speed')
plt.xlabel('Average Wind Speed, mph')
plt.ylabel('Number of days')
plt.xlim(-1, 21)

plt.tight_layout()
plt.show()

# plot 3
min_temp_plt3x = []
avg_windspeed_plt3y = avg_windspeed
for day in days:
    min_temp_plt3x.append(int(day[-1]))

plt.scatter(min_temp_plt3x, avg_windspeed_plt3y, color='k', marker='.', s=55)
plt.title('Average Wind Speed vs Minimum Temperature')
plt.xlabel('Minimum Temperature, F')
plt.ylabel('Average Wind Speed, mph')
plt.show()

# plot 4
plt4x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temp_min_jan = []
temp_max_jan = []
temp_min_feb = []
temp_max_feb = []
temp_min_mar = []
temp_max_mar = []
temp_min_apr = []
temp_max_apr = []
temp_min_may = []
temp_max_may = []
temp_min_jun = []
temp_max_jun = []
temp_min_jly = []
temp_max_jly = []
temp_min_ags = []
temp_max_ags = []
temp_min_spt = []
temp_max_spt = []
temp_min_oct = []
temp_max_oct = []
temp_min_nvb = []
temp_max_nvb = []
temp_min_dec = []
temp_max_dec = []
temp_avg_jan = []
temp_avg_feb = []
temp_avg_mar = []
temp_avg_apr = []
temp_avg_may = []
temp_avg_jun = []
temp_avg_jly = []
temp_avg_ags = []
temp_avg_spt = []
temp_avg_oct = []
temp_avg_nvb = []
temp_avg_dec = []


for day in days:
    if day[0][:2] == '1/':
        temp_max_jan.append(int(day[-2]))
        temp_min_jan.append(int(day[-1]))
        temp_avg_jan.append(int(day[3]))
    if day[0][:2] == '2/':
        temp_max_feb.append(int(day[-2]))
        temp_min_feb.append(int(day[-1]))
        temp_avg_feb.append(int(day[3]))
    if day[0][:2] == '3/':
        temp_max_mar.append(int(day[-2]))
        temp_min_mar.append(int(day[-1]))
        temp_avg_mar.append(int(day[3]))
    if day[0][:2] == '4/':
        temp_max_apr.append(int(day[-2]))
        temp_min_apr.append(int(day[-1]))
        temp_avg_apr.append(int(day[3]))
    if day[0][:2] == '5/':
        temp_max_may.append(int(day[-2]))
        temp_min_may.append(int(day[-1]))
        temp_avg_may.append(int(day[3]))
    if day[0][:2] == '6/':
        temp_max_jun.append(int(day[-2]))
        temp_min_jun.append(int(day[-1]))
        temp_avg_jun.append(int(day[3]))
    if day[0][:2] == '7/':
        temp_max_jly.append(int(day[-2]))
        temp_min_jly.append(int(day[-1]))
        temp_avg_jly.append(int(day[3]))
    if day[0][:2] == '8/':
        temp_max_ags.append(int(day[-2]))
        temp_min_ags.append(int(day[-1]))
        temp_avg_ags.append(int(day[3]))
    if day[0][:2] == '9/':
        temp_max_spt.append(int(day[-2]))
        temp_min_spt.append(int(day[-1]))
        temp_avg_spt.append(int(day[3]))
    if day[0][:2] == '10':
        temp_max_oct.append(int(day[-2]))
        temp_min_oct.append(int(day[-1]))
        temp_avg_oct.append(int(day[3]))
    if day[0][:2] == '11':
        temp_max_nvb.append(int(day[-2]))
        temp_min_nvb.append(int(day[-1]))
        temp_avg_nvb.append(int(day[3]))
    if day[0][:2] == '12':
        temp_max_dec.append(int(day[-2]))
        temp_min_dec.append(int(day[-1]))
        temp_avg_dec.append(int(day[3]))

max_month_temp = []
max_month_temp.append(max(temp_max_jan))
max_month_temp.append(max(temp_max_feb))
max_month_temp.append(max(temp_max_mar))
max_month_temp.append(max(temp_max_apr))
max_month_temp.append(max(temp_max_may))
max_month_temp.append(max(temp_max_jun))
max_month_temp.append(max(temp_max_jly))
max_month_temp.append(max(temp_max_ags))
max_month_temp.append(max(temp_max_spt))
max_month_temp.append(max(temp_max_oct))
max_month_temp.append(max(temp_max_nvb))
max_month_temp.append(max(temp_max_dec))

min_month_temp = []
min_month_temp.append(min(temp_min_jan))
min_month_temp.append(min(temp_min_feb))
min_month_temp.append(min(temp_min_mar))
min_month_temp.append(min(temp_min_apr))
min_month_temp.append(min(temp_min_may))
min_month_temp.append(min(temp_min_jun))
min_month_temp.append(min(temp_min_jly))
min_month_temp.append(min(temp_min_ags))
min_month_temp.append(min(temp_min_spt))
min_month_temp.append(min(temp_min_oct))
min_month_temp.append(min(temp_min_nvb))
min_month_temp.append(min(temp_min_dec))

avg_temp_month = []
avg_temp_month.append(sum(temp_avg_jan)/len(temp_max_jan))
avg_temp_month.append(sum(temp_avg_feb)/len(temp_max_feb))
avg_temp_month.append(sum(temp_avg_mar)/len(temp_max_mar))
avg_temp_month.append(sum(temp_avg_apr)/len(temp_max_apr))
avg_temp_month.append(sum(temp_avg_may)/len(temp_max_may))
avg_temp_month.append(sum(temp_avg_jun)/len(temp_max_jun))
avg_temp_month.append(sum(temp_avg_jly)/len(temp_max_jly))
avg_temp_month.append(sum(temp_avg_ags)/len(temp_max_ags))
avg_temp_month.append(sum(temp_avg_spt)/len(temp_max_spt))
avg_temp_month.append(sum(temp_avg_oct)/len(temp_max_oct))
avg_temp_month.append(sum(temp_avg_nvb)/len(temp_max_nvb))
avg_temp_month.append(sum(temp_avg_dec)/len(temp_max_dec))

plt.plot(plt4x, max_month_temp, 'r-', label='High T')
plt.plot(plt4x, min_month_temp, 'b-', label='Low T')
plt.bar(plt4x, avg_temp_month, color='orange')
plt.ylabel('Average Temperature, F')
plt.xlabel('Month')
plt.title('Temperature by Month')
plt.xlim(0, 13, 1)
plt.legend(loc='upper left')
plt.xticks(plt4x)
plt.show()
