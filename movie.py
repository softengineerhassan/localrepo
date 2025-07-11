class movie:
    def __init__(self,title,director,year):
        self.title = title
        self.director = director
        self.year = year

    def displayInformation(self):
        print(f"The name of movie is{self.title} the name of director is {self.director} and the year is {self.year}")




m1 = movie("Titanic","Hassan",2001)
m1.displayInformation()
m2 = movie("mirzapur","ali",2023)
m2.displayInformation()