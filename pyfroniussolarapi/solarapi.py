#! /usr/bin/env python
import json
import urllib
import urllib2
import datetime
import matplotlib

class solarapi:
    def __init__(self,host,verbose=False):
        self.host = host
        self.verbose = verbose
        return

    def PrintFormatted(self,paramdict):
        if not self.verbose:
            return
        print ">"*80
        for item in paramdict:

            v = False
            u = False
            #print paramdict[item]
            if type(paramdict[item]) is dict:
                if "Unit" in paramdict[item].keys():
                    u = paramdict[item]["Unit"]
                if "Value" in paramdict[item].keys():
                    v = paramdict[item]["Value"]
                elif "Values" in paramdict[item].keys():
                    v = paramdict[item]["Values"]

            if u and v:
                print "%s\t= %s %s"%(item,v,u)
            else:
                print "%s\t= %s"%(item, paramdict[item])
        print "<"*80

    def DoRequest(self,url,params):
        full_url = "http://"+self.host+url+"?"+urllib.urlencode(params)
        data = json.loads(urllib2.urlopen(full_url).read())

        if self.verbose:
            print "---- "+full_url+" ----"

        errorcode = data["Head"]["Status"]["Code"]
        errortext = data["Head"]["Status"]["Reason"]


        if not "Body" in data.keys() or errorcode >0:
            if self.verbose:
                print "%i - %s"%(errorcode,errortext)
            return False

        body = data["Body"]


        return data["Body"]

    def GetInverterRealtimeData(self,Scope="System",DeviceID=0,DataCollection="CumulationInverterData"):
        """
        Scope = System / Device

        if Scope = Device:
            DeviceID = 0..99
            DataCollection = CumulationInverterData / CommonInverterData / 3PInverterData / MinMaxInverterData
        """

        request_url = "/solar_api/v1/GetInverterRealtimeData.cgi"
        body = self.DoRequest(request_url,{"Scope":Scope,"DeviceID":DeviceID,"DataCollection":DataCollection})
        if body:
            self.PrintFormatted(body["Data"])
            return body["Data"]
        else:
            return False

    def GetSensorRealtimeData(self):
        return "NOT IMPLEMENTED"

    def GetStringRealtimeData(self,Scope="Device",DeviceId=0,DataCollection="NowStringControlData",TimePeriod="Day"):
        request_url = "/solar_api/v1/GetStringRealtimeData.cgi"
        body = self.DoRequest(request_url,{"Scope":Scope,"DeviceId":DeviceId,"DataCollection":DataCollection,"TimePeriod":TimePeriod})
        if body:
            self.PrintFormatted(body["Data"])
            return body["Data"]
        else:
            return False


    def GetLoggerInfo(self):
        request_url = "/solar_api/v1/GetLoggerInfo.cgi"
        body = self.DoRequest(request_url,{})
        if body:
            self.PrintFormatted(body["LoggerInfo"])
            return body["LoggerInfo"]
        else:
            return False



    def GetLoggerLEDInfo(self):
        return "NOT IMPLEMENTED"

    def GetInverterInfo(self):
        return "NOT IMPLEMENTEND"

    def GetActiveDeviceInfo(self):
        return "NOT IMPLEMENTED"

    def GetMeterRealtimeData(self):
        return "NOT IMPLEMENTED"

    def GetArchiveData(self,Scope="System",SeriesType="Detail",HumanReadable="False",StartDate=False,EndDate=False,Channel=False,DeviceClass="Inverter",DeviceId=0):
        request_url = "/solar_api/v1/GetArchiveData.cgi"
        if not EndDate:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            EndDate = now # now
        if not StartDate:
            twoweeksago = ( datetime.datetime.now()  + datetime.timedelta(days=-14)).strftime('%Y-%m-%d %H:%M:%S')
            StartDate = twoweeksago # EndTime - 16d

        if Scope=="System":
            DeviceClass="" 
            DeviceId=""

        body = self.DoRequest(request_url,{"Scope":Scope,"SeriesType":SeriesType,"HumanReadable":HumanReadable,"StartDate":StartDate,"EndDate":EndDate,"Channel":Channel,"DeviceClass":DeviceClass,"DeviceId":DeviceId})
        print body["Data"]
        return body

    def GetAllArchiveData(self):
        archive_fetchem = ["TimeSpanInSec",\
        #"Digital_PowerManagementRelay_Out_1",\
        "EnergyReal_WAC_Sum_Produced",\
        #"InverterEvents","InverterErrors",\
        "Current_DC_String_1","Current_DC_String_2",\
        "Voltage_DC_String_1","Voltage_DC_String_2",\
        "Temperature_Powerstage",\
        "Voltage_AC_Phase_1","Voltage_AC_Phase_2","Voltage_AC_Phase_3",\
        "Current_AC_Phase_1","Current_AC_Phase_2","Current_AC_Phase_3",\
        "PowerReal_PAC_Sum"]

        complete_archive_data = dict()

        for item in archive_fetchem:
            data = self.GetArchiveData("System","Detail","True",False,False,item,"Inverter",1)["Data"]["inverter/1"]["Data"]

            vals = data[data.keys()[0]]["Values"] # is a dict
            unit = data[data.keys()[0]]["Unit"] # is a string

            complete_archive_data[item] = [vals,unit]

        return complete_archive_data

if __name__ == "__main__": # test
    api = solarapi("192.168.3.110",True)

    api.GetLoggerInfo()


    api.GetInverterRealtimeData("System")
    api.GetInverterRealtimeData("Device",1,"CumulationInverterData")
    api.GetInverterRealtimeData("Device",1,"CommonInverterData")
    api.GetInverterRealtimeData("Device",1,"3PInverterData")
    api.GetInverterRealtimeData("Device",1,"MinMaxInverterData")

    api.GetAllArchiveData()

    #for i in range(0,199):
    #    print i
    #    api.GetStringRealtimeData("Device",i)

