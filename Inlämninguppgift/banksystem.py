
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
    


    
    def account_last_updated(self,last_updated):
        last_updated = datetime.datetime.now()
        return last_updated
    
    def customer_name(self,name):
        name = f"Customer{i}"
        return name
    
    def balance(self,saldo):
        saldo = random.randint(1,5)
        return saldo
    
def find_account(customers_list:list[Customer],
                 account_number:str) -> Customer or None:
    if len(account_number) != 15:
        print ("account number is incorrect format.")
        return None
    for customer in customers_list:
        if customer.account_number == account_number:
            return customer
        if  int(customer.account_number.replace ("-","")) > int(account_number.replace( "-", "")):
            return f" sortcut happend, function ended"
    #return None

def get_customer_birthday() -> datetime.date:
    year = random.randint(1922,2000)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return datetime.date(year, month,day)

def format_account_number(count)-> str:
    count = random.randint(1,10**7)
    return f"1111-{count:010d}"
    


if __name__ == "__main__":


    customers_list = []
    sort_list = []
    start = time()*1000.0
    for i in range(10**7):
        customer = Customer(account_number=format_account_number(i), name=str(i), birthday=get_customer_birthday, saldo=int)
        customers_list.append(customer)
    has_dupes = len(customers_list) != len(set(customers_list))
    print(f"Dupes found {has_dupes} ")
    
        
    

    

    end = time()*1000.0
    elapsed_time_for_creating_customers = end - start
    print(f"this is how long it took to create customers: {elapsed_time_for_creating_customers} ms elsapsed")
    
    start = time()*1000.0
    customers_list.sort(key=lambda customer: customer.account_number)
    end = time()*1000.0
    elasped_time_sort= end - start
    print(f"This is how long it takes to sort all the customers: {elasped_time_sort} ms elsaped")
