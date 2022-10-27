class Airport:
    def __init__(self, iata, name, location, city, country, website, phone):
        self.__iata = iata
        self.__name = name
        self.__location = location
        self.__city = city
        self.__country = country
        self.__website = website
        self.__phone = phone
        self.__flightOperators = {}

    def getIata(self):
        return self.__iata

    def getName(self):
        return self.__name

    def getLocation(self):
        return self.__location

    def getCity(self):
        return self.__city

    def getCountry(self):
        return self.__country

    def getWebsite(self):
        return self.__website

    def getPhone(self):
        return self.__phone

    def getFlightOperators(self):
        return self.__flightOperators

    def setIata(self, iata):
        self.__iata = iata

    def setName(self, name):
        self.__name = name

    def setLocation(self, location):
        self.__location = location

    def setCity(self, city):
        self.__city = city

    def setCountry(self, country):
        self.__country = country

    def setWebsite(self, website):
        self.__website = website

    def setPhone(self, phone):
        self.__phone = phone

    def setFlightOperartors(self, flightOperators):
        self.__flightOperators = flightOperators