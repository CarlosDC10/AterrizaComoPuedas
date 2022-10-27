import requests
from airport import Airport

class controller:
    def __init__(self):
        self.__airports = {}

    def AddAirport(self, iata):
        url = "https://airport-info.p.rapidapi.com/airport"

        querystring = {"iata":iata}

        headers = {
            "X-RapidAPI-Key": "108c7f5582mshc21d14a4f92b988p1f31edjsnbdbe21df7051",
            "X-RapidAPI-Host": "airport-info.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            if("error" in data):
                return False
            else:
                name = data["name"]
                location = data["street"]
                city = data["city"]
                country = data["country"]
                website = data["website"]
                phone = data["phone"]
                self.__airports[iata] = Airport(iata,name,location, city,country,website,phone)
                return True

    def AddOperator(self, iata, operator, numPlanes):
        if(iata in self.__airports):
            air = self.__airports[iata]
            air.getFlightOperators()[operator] = numPlanes
            return True
        else:
            return False
    
    def DeleteOperator(self, iata, operator):
        if(iata in self.__airports):
            air = self.__airports[iata]
            if(operator in air.getFlightOperators()):
                del(air.getFlightOperators()[operator])
                return True
            else:
                return False
        else:
            return False
        
    def ListOperators(self, operator):
        list = []
        for air in self.__airports:
            port = self.__airports[air]
            if operator in port.getFlightOperators():
                list.append(port)
        if(len(list) == 0):
            return "That operator does not run in any saved airport"
        else:
            return list

    def ListAirport(self, operator, condition):
        if(condition == "all"):
            acum = 0
            for air in self.__airports:
                port = self.__airports[air]
                if operator in port.getFlightOperators():
                    acum = acum + port.getFlightOperators()[operator]
            return acum
        else:
            if(condition in self.__airports):
                air = self.__airports[condition]
                if(operator in air.getFlightOperators()):
                    return air.getFlightOperators()[operator]
                else:
                    return "That operator does not run in any saved airport"
            else:
                return "Not a saved airport"

    def DeleteAirport(self, iata):
        if(iata in self.__airports):
            air = self.__airports[iata]
            if(len(air.getFlightOperators())==0):
                del(air)

