from .APIProxy import APIProxy

class WeatherProxy(APIProxy):
    def __init__(self):
        APIProxy.__init__(self)
        self.values = {"exclude": "minutely,flags,hourly"}
    def run(self):
        self.rootUrl = "https://api.darksky.net/forecast/6ece04ca9b999d85b9eed1037314792e/"
        self.rootUrl += str(APIProxy.latitude) + ","
        self.rootUrl += str(APIProxy.longitude) + "/"
        self.data = APIProxy.makeCall(self.rootUrl, self.values, -1, self)

        #ends run function if there is an error in makeCall()
        if isinstance(self.data, str):
            return self.data


        return self.data
