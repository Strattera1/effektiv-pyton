
import random
from time import time, sleep
import datetime
from dataclasses import dataclass


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
    
def find_account(customer_dict:dict[Customer],
                 account_number:str) -> Customer or None:
    if len(account_number) != 15:
        print ("account number is incorrect format.")
        return None
    result = customer_dict.get(account_number)
    return result

    
def get_customer_birthday() -> datetime.date:
    year = random.randint(1922,2000)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return datetime.date(year, month,day)
 


def format_account_number(count:int)-> str:
    return f"1111-{count:010d}"


if __name__ == "__main__":

    milseconds = 1000
    start = time()
    customer_dict= {
        format_account_number(i): Customer(account_number=format_account_number(i),
                                            name=i,birthday=get_customer_birthday(), saldo=0) for  i in range(10**5)
        }  
      
    
    end = time()
    elapsed_time_for_creating_customers = end - start
    print(f"this is how long it took to create all customers: {elapsed_time_for_creating_customers:.5f}{elapsed_time_for_creating_customers * 1000:2f} ms elsapsed")

    total_time_1 = 0
    for m in range(milseconds):
        start = time()
        result_account1 = find_account(customer_dict,account_number="1111-0000001000")
        end = time()
        total_time_1 += (end-start)
    result_time_1 = total_time_1/milseconds
    print ("result: ",result_account1, f" {result_time_1:.5f} {result_time_1 * 1000:2f} millesceonds")


    total_time_2 = 0
    for m in range(milseconds):
        start = time()
        result_account2 = find_account(customer_dict,account_number="1111-0000099999")
        end = time()
        total_time_2 += (end-start)
    result_time_2 = total_time_1/milseconds
    print("Result:", result_account2, f" {result_time_2:.5f}{result_time_2 * 1000:2f} millesceonds to find")
    
    total_time_3 = 0
    for x in range(milseconds):
        start = time()
        result_account3 = find_account(customer_dict,account_number="1111-9999999999")
        end = time()
        total_time_3 += (end-start)
    result_time_3 = total_time_3/milseconds
    print("Result:", result_account3, f"{result_time_3:.5f}{result_time_3 *1000:2f} mileseconds,  account does not exist.")