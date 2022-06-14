import csv
import datetime as dt
import datetime
import time
with open('Jmeter_log2.jtl', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)  # skip the headers
    for i in reader:
        #print(i[3])
        #print(type(i[3]))
        if i[3] != '200':

            #print(type(i[0]))
            #print(int(i[0]))

            timestamp = i[0]
            your_dt = datetime.datetime.utcfromtimestamp(int(timestamp) / 1000)  # using the local timezone
            #print(your_dt.strftime("%Y-%m-%d %H:%M:%S"))
            print(your_dt.strftime("%Y-%m-%d %H:%M:%S"), i[2], i[3], i[4], i[8])


