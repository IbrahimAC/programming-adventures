import datetime

class Vehicles:

    currentYear = datetime.datetime.now().year

    def __init__(self, registrationNumber, vehicleManufacturer,):
        self.regNum = registrationNumber
        self.vMf = vehicleManufacturer
        # self.miles = None #these are none as we have not input anything when creating the instances originally
        # self.mDate = None

    @property
    def display(self):#1
        return'Registration Number: {}, Vehicle Manufacturer: {}'.format(self.regNum, self.vMf)
    # returns a string and substitutes out the placeholders ( these things{})
    # for our attributes for the specified instance, using .format

    def setNumberOfMiles(self, miles): #2
        self.miles = miles
    # Changes our miles attribute to whatever value we input

    def setYearOfManufacturer(self,year):#3
        self.mDate = year
    # Function changes our attribute to whatever value we input e.g. 1995

    @property
    def yearsActive(self): #4
        return Vehicles.currentYear - self.mDate
    # Our class variable on line 2 stores the current year, simple function
    # where we subtract the manufacturer date from the current year to give us the amount of years active

class civ(Vehicles):

    def __init__(self, wheels, doors, registrationNumber):
        super().__init__(registrationNumber, registrationNumber)
        self.wheels = wheels
        self.doors = doors

fiesta = civ(2,0,'UK 77HI')

class oldCars(Vehicles):
    def __init__(self, percentageOfRust, brokenWindows, vehicleManufacturer):
        super(oldCars, self).__init__(vehicleManufacturer, vehicleManufacturer)
        self.rust = percentageOfRust
        self.bwin = brokenWindows

    @property
    def getFixable(self):
        if self.yearsActive > 30 or self.rust > 60:
            return 'This Car cant still be used'
        else:
            return 'This Car can be used'


corola = oldCars(78,3, 'Toyota')
corola.setYearOfManufacturer(2000)
# print(fiesta.getFixable) # my subclass doesnt have access to the method in my other subclass
print(corola.getFixable)


# print(fiesta.regNum)
# fiesta.setYearOfManufacturer(2000)
# print(fiesta.yearsActive)
# using the @property allows us to access the function as an attribute
# print(Vehicles.yearsActive(limo))

pickupTruck = Vehicles('UK PL8TE', 'Ford',)
limo = Vehicles('UK SP4D3', 'Rolls Royce',)
limo.regNum = 'US H8TE'
limo.setNumberOfMiles(566)
limo.setYearOfManufacturer(1996)


#Tasks:
# Create an Vehicle Class and initialize it with registration number and Car Manufacturer
# Create an Vehicle Class and initialize it with registration number and Car Manufacturer. Make methods to:
# 1. Display (EASY) - It should display all information about the vehicle (format how you want)
# 2. setNumberOfMiles (EASY) - It should assign the vehicle millage to the vehicle
# 3. setYearOfManufacturer (EASY) - It should assign the year the vehicle was manufactured to the vehicle
# 4. yearsActive (MEDIUM) - It should calculate the number of years since the car was manufactured