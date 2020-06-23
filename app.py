from bike_rental import BikeRental,Customer
def main():
    shop=BikeRental(50)
    customer=Customer()
    while True:
        print("""
            ====== Bike Rental Shop =======
            1. Display available bikes
            2. Request a bike on hourly basis $5
            3. Request a bike on daily basis $20
            4. Request a bike on weekly basis $60
            5. Return a bike
            6. Exit
            """)
        choice=int(input("Enter your choice: "))
        if choice==1:
            shop.displayBike()
        elif choice==2:
            customer.rentalTime=shop.rentBikeHourly(customer.requestBike())
            customer.rentalBasis=1
        elif choice==3:
            customer.rentalTime=shop.rentBikeDaily(customer.requestBike())
            customer.rentalBasis=2
        elif choice==4:
            customer.rentalTime=shop.rentBikeweekly(customer.requestBike())
            customer.rentalBasis=3
        elif choice==5:
            customer.bill=shop.returnBike(customer.returnBike())
            customer.rentalBasis,customer.numOfBikes,customer.rentalTime=0,0,0




if __name__ == "__main__":
    main()