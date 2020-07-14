import urllib
import urllib.request
import urllib.parse
import json
from abc import ABC

class APIProxy(ABC):
    #Class variables needed for proxies to operate
    name = ""
    latitude = ""
    longitude = ""
    #Create Logs using chain of responsibility
    #log1 = Log.TeleportLog()
    #log2 = Log.ZomatoLog(log1)
    #log3 = Log.DarkSkyLog(log2)



    def __init__(self):
        self.data = ""
        self.rootUrl = ""


    #Encapsulates Connection Details
    def makeCall(rootUrl, values, header, callerType):
        tempUrl = rootUrl
        count = 0
        #Could I use self.data here?
        data = ""
        for x in values:
            if count == 0:
                tempUrl += "?" + str(x) + "=" + str(values[x])
            else:
                tempUrl += "&" + str(x) + "=" + str(values[x])
            count += 1

        tempUrl = tempUrl.replace(" ", "%20")
        if header != -1:
            try:
                req = urllib.request.Request(tempUrl,headers = header)
                resp = urllib.request.urlopen(req)
                data = json.load(resp)
            except Exception as e:
                #APIProxy.log3.handle_request(data, tempUrl, callerType)
                return str(e) + "\nError connecting to " + tempUrl

        else:
            try:
                x = urllib.request.urlopen(tempUrl)
                data = json.load(x)
            except Exception as e:
                #APIProxy.log3.handle_request(data, tempUrl, callerType)
                return str(e) + "\nError connecting to " + tempUrl

        #APIProxy.log3.handle_request(data, tempUrl, callerType)
        return data

    def run(self):
        pass
