from  .APIProxy import APIProxy

class FoodProxy(APIProxy):
    def __init__(self):
        APIProxy.__init__(self)
        self.values = {}
        self.header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "db440c55fdec3626b4aca07f00a3623d"}

    def run(self):
            self.rootUrl = "https://developers.zomato.com/api/v2.1/locations?"
            self.values["query"] = self.name
            self.values["lat"] = self.latitude
            self.values["lon"] = self.longitude
            self.data = APIProxy.makeCall(self.rootUrl, self.values, self.header, self)

            #ends run function if there is an error in makeCall()
            if isinstance(self.data, str):
                return self.data

            entityType = self.data["location_suggestions"][0]["entity_type"]
            entityID = self.data["location_suggestions"][0]["entity_id"]

            tempVal = {"entity_id": str(entityID), "entity_type": str(entityType)}
            self.rootUrl = "https://developers.zomato.com/api/v2.1/location_details"
            self.data = APIProxy.makeCall(self.rootUrl, tempVal, self.header, self)

            #ends run function if there is an error in makeCall()
            if isinstance(self.data, str):
                return self.data

            return self.data

            # print()
            # print(APIProxy.APIProxy.name)
            # print ("----------------------")
            # print("Popularity Rating:", self.data["popularity"] + "/5.00")
            # print("Night Life Rating:", self.data["nightlife_index"] + "/5.00")
            # print("Top Cuisines:")
            # for x in self.data["top_cuisines"]:
            #     print("-", x)
            # print("Most Highly Rated Restaurants:", )
            # for x in  self.data["best_rated_restaurant"]:
            #     print("-", x["restaurant"]["name"], "\n\t", x["restaurant"]["location"]["address"])
            # print()
            #
            # return "good"
