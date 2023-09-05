
import random
from time import time, sleep
import datetime
# alphabet = ("A", "B", "C", "D", "E", "F",
#             "G", "H", "I", "J", "K", "L",
#             "M", "N", "O", "P", "Q", "R",
#             "S", "T", "U", "V", "W", "X", 
#             "Y", "Z")
# DOB = (
#      datetime.date(1992,1,1),
#      datetime.date(1938,12,14),
#      datetime.date(1972,3,15)
# )

# Behöver fixa till kononummer systemet. Nummern ska gå ner i sekvens ordning. 
# Börja med att skapa en random födelsdag lista
def get_account_number(start,end,prefix = "1111-"):
    account_numbers = []
    for i in range (start,end + 1):
            account_number = f"{prefix}{i:010}"
            account_numbers.append(account_number)
    return account_numbers
class Customer:

    def __init__(self,name:str, birthday:int, account_number:str or None, saldo:int):
        # self.created = created
        # self.last_updated = last_updated
        # self.name = name
        # self.birthday= birthday
        # self.account_number= account_number
        # self.saldo = saldo
        self.created = self.account_created(time)
        self.last_updated = self.account_last_updated(datetime)
        self.name = self.customer_name(str)
        self.birthday= self.customer_birthday(int)
        self.account_number= account_number
        self.saldo = self.balance(saldo)
        

    
    
    def __repr__(self) -> str:
        return f"Customer(Account Number: {self.account_number}, Name: {self.name}:{self.saldo}:{self.birthday})"
    



    # def get_account_number(account_number, i):
    #     total_zero = "0000000000"
    #     for last_account_number in range (1,100000001):
    #         total_zero = total_zero[len(total_zero) - len(str(last_account_number)) + 1]
    #         account_number = f"1111-{total_zero}{last_account_number: 010d}"
            
    #     return account_number

        
    def customer_birthday(self,birthday):
        self.birthday = []
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
    
    def account_created(self,created):
        # self.created = []
        # created = datetime.datetime.now()
        return time()
    
    def account_last_updated(self,last_updated):
        self.last_updated = []
        last_updated = datetime.datetime.now()
        return last_updated
    
    def customer_name(self,name):
        self.name = []
        name = f"Customer{i+ 1}"
        return name
    
    def balance(self,saldo):
        self.saldo = []
        saldo == f"{random.randint(1,40000)}"
        return saldo
    
def find_account(customers:list[Customer],
                account_number: str ) -> Customer or None:
    search_area = get_sublist_of_accounts(customers,account_number)
    for customer in search_area:
        if customer.account_number == account_number:
            return customer
    return None

def get_sublist_of_accounts( customers: list[list[Customer]]
                            ,account_number:str) -> Customer:
    return customers(account_number[0])
        

    
if __name__ == "__main__":
    customers = []
    # for letter in alphabet:
    #     customers.append([])

    # for i in range (10 ** 7):
    #     customer = Customer(created=any ,last_updated=datetime,name=str,birthday=int,account_number=str,saldo=int)
    #     customers.append(customer)
    start = time()    
    for i in range(10**4):
        customer = Customer(account_number=i, name=str, birthday=int, saldo=int)
        customers.append(customer)
    end = time()
    elapsed_time_for_creating_customers = end - start
    for i in customers:
        print(i)
    print(f"this is how long it took to create customer{elapsed_time_for_creating_customers}")

    # for customer_result in customers:
    #     start = time()
    #     customer_result = [customers[10000]]
    #     end = time()
    # print( customer_result[0], f"took {end - start} seconds to find")