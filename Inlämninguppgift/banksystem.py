
import random
from time import time, sleep
import datetime


# Den hämtar sifforna två gånger. 



    # def get_account_number(account_number, i):
    #     total_zero = "0000000000"
    #     for last_account_number in range (1,100000001):
    #         total_zero = total_zero[len(total_zero) - len(str(last_account_number)) + 1]
    #         account_number = f"1111-{total_zero}{last_account_number: 010d}"
            
    #     return account_number



#Kan ej ha funktionen inne i klassen.Den måste vara utanför. 
#Verkar som att jag inte kallar på funktionen någonstans. behövs fixa. 
class Customer:

    def __init__(self,name:str, birthday:int, account_number :str, saldo:int):
        self.created = self.account_created(time)
        self.last_updated = self.account_last_updated(datetime)
        self.name = self.customer_name(str)
        self.birthday= self.customer_birthday(int)
        self.account_number= f"111-{account_number:010d}"
        self.saldo = self.balance()

    
    
    def __repr__(self) -> str:
        return f"Customer(Account Number: {self.account_number}, Name: {self.name})"
    



        
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
    start = time()    
    for i in range(10**3):
        customer = Customer(account_number=i, name=str, birthday=int, saldo=int)
        customers.append(customer)
    end = time()
    elapsed_time_for_creating_customers = end - start
    for i in customers:
        print(i)
    print(f"this is how long it took to create customer{elapsed_time_for_creating_customers}")
