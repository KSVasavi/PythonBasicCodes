class car:
    def __init__(self):
        self.cgst=5555
        self.sgst=5555
        self.insurance=5555
    def company(self):
        while True:
            print("T,M")
            self.n=input("Enter the car company")
            if self.n=="T":
                print("me, TOYOTA")
                self.model()
                break
            elif self.n=="M":
                print("me, MERCEDES")
                self.model()
                break
            else:
                print("Enter valid company")
    def model(self):
        if self.n=="T":
            while True:
                print("Select from fortuner and lc")
                self.choice=input("Enter the car model")
                if self.choice=="F":
                    self.price(self.choice)
                    break
                elif self.choice=="LC":
                    self.price(self.choice)
                    break
                else:
                    print("Invalid")
        elif self.n=="M":
            while True:
                print("Select from amg and gw")
                self.choice=input("enter car model")
                if self.choice=="AMG":
                    self.price(self.choice)
                    break
                elif self.choice=="GW":
                    self.price(self.choice)
                    break
                else:
                    print("Invalid")
    def price(self,choice):
        if choice=="F":
            self.p=1000000
        elif choice=="LC":
            self.p=1300000
        elif choice=="AMG":
            self.p=1400050
        elif choice=="GW":
            self.p=500000
        total_p=self.p+self.sgst+self.cgst+self.insurance
        print(total_p)
c=car()
c.company()        