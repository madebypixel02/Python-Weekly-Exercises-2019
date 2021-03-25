import random
class Island:
    def __init__(self, name, coordenates, country, appropriate):
        self.__name = name
        self.__coordenates = coordenates
        self.__country = country
        self.__appropriate = appropriate
    
    @property
    def name(self):
        return self.__name
    @property
    def appropriate(self):
        return self.__appropriate
    
    
    
    
        
class Plane:
    def __init__(self, id, origin, destination, passengers, company):
        self.__id = id
        self.__origin = origin
        self.__destination = destination
        self.__passengers = passengers
        self.__status = random.choice(['on time', 'delayed', 'cancelled'])
    
    @property
    def origin(self):
        return self.__origin
    @property
    def destination(self):
        return self.__destination

    def fly(self):
        if len(self.__passengers) == 0:
            print('There are no passengers!')
        
        else:
            if self.__status == 'cancelled':
                print('Sorry, flight has been cancelled')
            elif not self.__destination.appropriate:
                print("It's too dangerous to fly to", self.__destination.name, "as it is not habitable.")
            else:
                print("Plane with ID", self.__id, "flew from", self.__origin.name, "to", self.__destination.name, "with status:", self.__status)
                for i in range(len(self.__passengers)):
                    print("welcome to", self.__destination.name, self.__passengers[i].name)
        
class Passenger:
    def __init__(self, name, id, flight_id):
        self.__name = name
        self.__id = id
        self.__flight_id = flight_id
    
    @property
    def name(self):
        return self.__name
        
    
        