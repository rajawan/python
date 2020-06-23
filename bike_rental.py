import datetime

class BikeRental:
    def __init__(self,stock:int=0):
        #our constructor class that instantiates bike rental shop
        self.stock=stock
    def displayBike(self):
        print(f' We have currently {self.stock} avaliable bikes') 

    def rentBikeHourly(self,num):
        if num<0:
            print('Number of bike should be positive')
            return None
        elif num>self.stock:
            print(f'Sorry currently we have {self.bike} bikes')
            return None
        else:
            now=datetime.datetime.now()
            print(f'You have rented a bike on Hourly basis at {now}')
            print('You will be charge $5 per hour each bike')
            print('Hope youj enjoy our service')
            self.stock-=num
            return now

    def rentBikeDaily(self,num):
        if num<0:
            print('Number of bike should be positive')
            return self.stock
        elif num>self.stock:
            print(f'Sorry currently we have {self.bike} bikes')
        else:
            now=datetime.datetime.now()
            print(f'You have rented a bike on daily basis at {now}')
            print('You will be charge $20 per day each bike')
            print('Hope you enjoy our service')
            self.stock-=num
            return now

    def rentBikeweekly(self,num):
        if num<0:
            print('Number of bike should be positive')
            return self.stock
        elif num>self.stock:
            print(f'Sorry currently we have {self.bike} bikes')
        else:
            now=datetime.datetime.now()
            print(f'You have rented a bike on Hourly basis at {now}')
            print('You will be charge $60 per week each bike')
            print('Hope youj enjoy our service')
            self.bike-=num
            return now

    def returnBike(self, request):
        """
        1.accept bike from the customer
        2.redecorate the inventory
        3.return bill to the customer
        """
        rentalBasis, numofBikes, rentalTime = request
        bill=0
        if rentalTime and rentalBasis and numofBikes:
            self.stock=numofBikes+self.stock
            now=datetime.datetime.now()
            renttime=now-rentalTime
            if rentalBasis==1:
                bill=round(renttime.seconds/3600)*5*numofBikes
            elif rentalBasis==2:
                bill=round(renttime.days)*20*numofBikes
            elif rentalBasis==3:
                bill=round(renttime.days/7)*60*numofBikes
            if (3<=numofBikes<=5):
                print("You will eligiable for family promotion at 30% discount")
                bill=bill*0.7
            print("Thanks for returning your bikes")   
            print(f"Your total bill {bill}")
            return bill
        else:
            print("Are you sure you rent a car")
            return None
class Customer:
    def __init__(self):
        self.rentalBasis=0
        self.numofBikes=0
        self.rentalTime=0
        self.bill=0

    def requestBike(self):
        #take a rquest from the customer for the number of bikes
        bikes=int(input("How many bikes would you want to rent: "))
        if bikes<1:
            print("Num of bikes should be greater than zero!")
            return -1
        else:
            self.numofBikes=bikes
        return self.numofBikes
    def returnBike(self):
        #Allow customer to return their bike
        if self.rentalBasis and self.numofBikes and self.rentalTime:
            return self.rentalBasis, self.numofBikes, self.rentalTime
        else:
            return 0,0,0
    