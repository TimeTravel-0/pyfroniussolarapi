#!/usr/bin/env python

from pyfroniussolarapi import solarapi
import pickle
import csv


def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


#api = solarapi.solarapi("192.168.3.110",True)
#data = api.GetAllArchiveData()
#save_obj(data,"archivedata")

data = load_obj("archivedata")


f = open("archivedata.csv", 'wt')
try:
    writer = csv.writer(f)

    mainkeys = data.keys()

    writer.writerow( ['']+mainkeys )


    timekeys = []
    for columnno in range(0,len( data.keys() )):
        column_timekeys = data[ data.keys()[columnno] ][0].keys()
        timekeys+=column_timekeys

    # remove duplicates and sort ascending
    timekeys = list(set(timekeys))
    timekeys.sort(key=int)

    for timekey in timekeys:
        row = [timekey]
        for columnname in mainkeys:
            if timekey in data[columnname][0]:
                row+=[data[columnname][0][timekey]]
            else:
                row+=[0]
        writer.writerow( row )

finally:
    f.close()

#print data.keys()
