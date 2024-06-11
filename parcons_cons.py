class ice_cream:
    def __init__(self,imp,notimp):
        self.imp1=imp
        self.notimp1=notimp
        print("COMPULSORY IN THE START NEEDED")
    def factory(self):
        print("In the making, assembling raw ingredients")
        self.pr= 10000
    def shop(self):
        print("No of pieces")
        dem="Good"
        print(dem)
    def customer(self):
        print("My favorite flavour is chocolate, I need")
        cus=self.pr - 9999
        print(cus)
        print("important"+self.imp1)
        print("Not important"+self.notimp1)
food=ice_cream("quality","quantity")
food.factory()
food.shop()
food.customer()     