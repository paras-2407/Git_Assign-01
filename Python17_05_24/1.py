class Car:
    def __init__(self, make, model,year) -> None:
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        print(f"Company of the car {self.make}, models of the car {self.model}, year of the car manufacture {self.year}")


c=Car("VW", "Polo", 2015)
c.display_info()