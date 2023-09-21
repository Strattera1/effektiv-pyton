
import random
from time import time, sleep
import datetime




class Customer:

    def __init__(self,name:str, birthday:datetime.date, account_number :str, saldo:int):
        self.account_number= account_number
        self.name = self.customer_name(name)
        self.birthday = birthday
        self.saldo = self.balance(int)
        self.created = time()
        self.last_updated = self.account_last_updated(datetime)

    
    
    def __repr__(self) -> str:
        return f"Customer( Account Number: {self.account_number})"
    



        
    
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

def get_customer_birthday() -> datetime.date:
    year = random.randint(1922,2000)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return datetime.date(year, month,day)

def format_account_number(count:int)-> str:
    return f"1111-{count:010d}"  

if __name__ == "__main__":


    customers = []
    start = time()    
    for i in range(10**7):
        customer = Customer(account_number=format_account_number(i), name=i, birthday=get_customer_birthday, saldo=int)
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
    print ("result: ",result_account3, f" seconds to find {end-start}, account does not exist.")