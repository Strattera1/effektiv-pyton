
import random
from time import time, sleep
import datetime
alphabet = ("A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X", 
            "Y", "Z")
DOB = (
     datetime.date(1992,1,1),
     datetime.date(1938,12,14),
     datetime.date(1972,3,15)
)

# Behöver fixa till kononummer systemet. Nummern ska gå ner i sekvens ordning. 
# Börja med att skapa en random födelsdag lista

class Customer:

    def __init__(self,created,last_updated,name, birthday, account_number, saldo):
        self.created = datetime.datetime.now()
        self.last_updated = datetime.datetime.now()
        self.name = name
        self.birthday= birthday
        self.account_number= account_number
        self.saldo = saldo
    
    def __repr__(self) -> str:
        return f"Customer({self.birthday})"
    
    def assign_random_birthday(self):
        #birthday_date = datetime.now("%Y %m %D")
        self.birthday = random.choice(DOB)

    def get_account_number(self,end,prefix = "1111-"):
        self.account_number = []
        for i in range (start,end + 1):
              self.account_number = f"{prefix}{i:010}"
              self.account_number.append(self.account_number)
        return self.account_number
        
    def birthday(birthday):
        year = birthday(random.randint(1922,2000))
        month = birthday(random.randint(1,12))
        day = birthday(random.randint(1,31))
        if month == 2:
            day= random.randint(1,28)
        elif month == 4 and month == 6 and month == 9 and month == 11:
            day = random.randint(1,30)
        else:
            day = random.randint(1,31)
        return year, month,day 
    
# def get_sublist_of_birthday(customers: list [list[Customer]],
#                                 birthday_date: str) -> list[Customer]:
#         return customers[alphabet.index(birthday_date[0])]

    
if __name__ == "__main__":
    customers = []
    for letter in alphabet:
        customers.append([])

    for i in range (10 ** 7):
        customer = Customer()
        Customer(created=)


    start = time()

    end = time()
    print(, f"took {end - start} seconds to find")