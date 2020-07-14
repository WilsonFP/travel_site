from  .APIProxy import APIProxy

class LocationProxy(APIProxy):
    def __init__(self, destination):
        APIProxy.__init__(self)
        self.values = {"search" : destination}

    def run(self):
        self.rootUrl = "https://api.teleport.org/api/cities/"

        self.data = APIProxy.makeCall(self.rootUrl, self.values, -1, self)

        if isinstance(self.data, str):
            return self.data

        return self.data

    def set_data(self, old_data, selected_result):
        temp_array = selected_result.split(' ')

        APIProxy.name = old_data["_embedded"]["city:search-results"][int(temp_array[0])-1]["matching_full_name"]

        #Make another call to API for latitude and longitude
        self.data = APIProxy.makeCall(old_data["_embedded"]["city:search-results"][int(temp_array[0])-1]["_links"]["city:item"]["href"], {}, -1, self)

        #ends run function if there is an error in makeCall()
        if isinstance(self.data, str):
            return self.data

        APIProxy.latitude = self.data["location"]["latlon"]["latitude"]
        APIProxy.longitude = self.data["location"]["latlon"]["longitude"]
