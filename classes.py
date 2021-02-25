# creating a class. it will have init method
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x, p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_new(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

        
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ['Hima', 'Bindu', 'Appali', 'Rag']
for person in people:
    if(flight.add_new(person)):
        print('added pass', person)
    else:
        print(f'The max capacity is {flight.capacity}. You reached max capacity')



