#example one
class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    numOfRooms = 5
    bathrooms = 2
    def cost_of_evaluation(self):
        print(self.numOfRooms)
        pass

obj_home = House()
'''
print (obj_home.numOfRooms)
print (obj_home.bathrooms)
obj_home.cost_of_evaluation()
'''
#Here we are only changing the instance attribute 
obj_home.numOfRooms = 7
print(obj_home.numOfRooms)
print(House.numOfRooms)

#Here we are changing the class attribute
House.numOfRooms = 7
print(obj_home.numOfRooms)
print(House.numOfRooms)

