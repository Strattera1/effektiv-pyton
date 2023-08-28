import random
from time import time, sleep
alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Z")

class Car:
    """
    This class is for license plate for cars.
    """
    def __init__(self, license_plate:str = None):
        if license_plate is None:
            self.assign_random_license_plate()
        else:
            self.license_plate = license_plate

    def __repr__(self) -> str:
        return f"Car({self.license_plate})"

    def assign_random_license_plate(self):
        license_numbers = random.randint(111, 999)
        license_chars = ""
        for i in range(3):
            character = random.choice(alphabet)
            license_chars += character
        self.license_plate = f"{license_chars}{license_numbers}"

def get_car_by_license_plate(cars:list[Car],
                             license_plate:str) -> Car or None:
    search_area = get_sublist_of_plates(cars, license_plate)
    for car in search_area:
        if car.license_plate == license_plate:
            return Car
    return None

def get_sublist_of_plates(cars: list[list[Car]],
                                license_plate :str) -> list [Car]:
    return cars[alphabet.index(license_plate[0])]

if __name__== "__main__":
    # This code only runs if I explicitly run this file.
    
    
    cars = []

    for letter in alphabet:
        cars.append([])
    
    for i in range(10 **6):
        car = Car()
        
        car_underlist= get_sublist_of_plates(cars, car.license_plate)
        car_underlist.append(car)

    volvo = Car(license_plate="BBB123")
    car_underlist = get_sublist_of_plates(cars, volvo.license_plate)
    car_underlist.append(volvo)

    volvo2 = Car(license_plate="ZBB123")
    car_sublist = get_sublist_of_plates(cars, volvo2.license_plate)
    car_sublist.append(volvo2)

#def find_car_by_license_plate(cars: list(Car)):

    

    start  = time()
    result_car = get_car_by_license_plate(cars, "ASS432")
    end = time()
    print ("Search result", result_car)

    start = time()
    result_car = get_car_by_license_plate(cars, "ZBB123")
    end = time()
    print(result_car, f"took {end - start} seconds to find")


