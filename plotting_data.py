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

print(days)
