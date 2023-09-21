
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
        name = f"Customer{name}"
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

    milseconds = 1000
    customers = []
    start = time()    
    for i in range(10**7):
        customer = Customer(account_number=format_account_number(i), name=i, birthday=get_customer_birthday, saldo=int)
        customers.append(customer)



    end = time()
    elapsed_time_for_creating_customers = end - start

    print(f"this is how long it took to create customers: {elapsed_time_for_creating_customers} seconds elsapsed")
    
    
    total_time_1 = 0
    for i in range (milseconds):
        start = time()
        result_account1 = find_account(customers,account_number="1111-0000001000")
        end = time()
        total_time_1 += (end-start)
    result_time_1 = total_time_1/milseconds
    print ("result: ",result_account1, f" ms to find {result_time_1:.5f}{result_time_1 * 1000:.2f}")


    total_time_2 = 0
    for i in range (milseconds):
        start = time()
        result_account2 = find_account(customers,account_number="1111-0009999999")
        end= time()
        total_time_2 += (end-start)
    result_time_2 = total_time_1/milseconds
    print ("result: ",result_account2, f" ms to find {result_time_2:.5f}{result_time_2 * 1000:.2f}")
    
    total_time_3 = 0
    for i in range (milseconds):
        start = time()
        result_account3 = find_account(customers,account_number="1111-9999999999")
        end = time()
        total_time_3 += (end-start)
    result_time_3 = total_time_1/milseconds
    print ("result: ",result_account3, f" ms to find  {result_time_3:.5f}{result_account3 * 1000:2f}, account does not exist.")