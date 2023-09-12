
import random
from time import time, sleep
import datetime




# Nästan klar med version 1. Behöver fixa så att konton kan upptäckas.
# problemet verkar ligga i rad 82. 
class Customer:

    def __init__(self,name:str, birthday:int, account_number :str, saldo:int):
        self.created = self.account_created(time)
        self.last_updated = self.account_last_updated(datetime)
        self.name = self.customer_name(str)
        self.birthday= self.customer_birthday(int)
        self.account_number= f"1111-{account_number:010d}"
        self.saldo = self.balance(int)

    
    
    def __repr__(self) -> str:
        return f"Customer(Account Number: {self.account_number}, Name: {self.name}, Birthday {self.birthday},\n\n Saldo: {self.saldo}, Created: {self.created}, Last Uppdated: {self.last_updated} )"
    



        
    def customer_birthday(self,birthday):
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
        last_updated = datetime.datetime.now()
        return last_updated
    
    def customer_name(self,name):
        name = f"Customer{i}"
        return name
    
    def balance(self,saldo):
        saldo = random.randint(1,40000)
        return saldo
    
def find_account(customers:list[Customer],
                 account_number:str) -> Customer or None:
    if len(account_number) != 15:
        print ("account number is incorrect format.")
        return None
    for customer in customers:
        if customer.account_number == account_number:
            return customer
    return None


        

if __name__ == "__main__":


    customers = []
    start = time()    
    for i in range(10**7):
        customer = Customer(account_number=i, name=str, birthday=int, saldo=int)
        customers.append(customer)



    end = time()
    elapsed_time_for_creating_customers = end - start

    print(f"this is how long it took to create customers: {elapsed_time_for_creating_customers} seconds elsapsed")

    start = time()
    result_account1 = find_account(customers,account_number="1111-0000500000")
    end = time()
    print ("result: ",result_account1, f" seconds to find {end-start}")

    start = time()
    result_account2 = find_account(customers,account_number="1111-0009999999")
    end= time()
    print ("result: ",result_account2, f" seconds to find {end-start}")
    
    start = time()
    result_account3 = find_account(customers,account_number="1111-9999999999")
    end = time()
    print ("result: ",result_account3, f" seconds to find {end-start}")