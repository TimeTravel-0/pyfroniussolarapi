#!/usr/bin/env python

from pyfroniussolarapi import solarapi

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


api = solarapi.solarapi("192.168.3.110",True)

data = api.GetAllArchiveData()

save_obj(data,"archivedata")
