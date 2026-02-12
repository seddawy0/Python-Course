class Car:
    def __init__(self, carModel, carYear, carColor, forSale): # Attributes
        self.model = carModel
        self.year = carYear
        self.color = carColor
        self.sale = forSale
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    def carInfo(self):
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
        print(f"Car Color: {self.color}")
        print(f"For Sale: {self.sale}")