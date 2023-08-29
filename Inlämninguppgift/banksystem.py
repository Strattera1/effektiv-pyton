
import random
from time import time, sleep
import datetime
alphabet = ("A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X", 
            "Y", "Z")

# Börja med att skapa en random födelsdag lista

class Customer:

    def __init__(self, birthday:str = None):
        if birthday is None:
            self.assign_random_birthday()
        else:
            self.birthday = birthday
    
    def __repr__(self) -> str:
        return f"Customer({self.birthday})"
    
    def assign_random_birthday(self):
        birthday_date = random.datetime("%Y- %b-%d")
        self.birthday = f"{birthday_date}"

    def find_customer_by_birthdate(customers:list [Customer],
                                   birthday:str) -> Customer or None:
        search_area= get_sublist_of_birthday(customers,birthday)
        for customer in search_area:
            if customer.birthday == birthday:
                return customer
        return None
    
    def get_sublist_of_birthday(customers: list [list[Customer]],
                                birthday_date: str) -> list[Customer]:
        return customers[alphabet.index(birthday_date[0])]
    
    if __name__ == "__main__":
        customers = []
        for letter in alphabet:
            customers.append([])

        for i in range (10 ** 5):
            customer = Customer()

            customer_sublist = get_sublist_of_birthday(customers, customers.birthday_date)
            customer_sublist.append(customer)
        
        user = Customer(birthday = "1992 may 25")