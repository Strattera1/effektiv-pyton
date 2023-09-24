
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
    
def find_account(customers_list:list[Customer],
                 account_number:str) -> Customer or None:
    if len(account_number) != 15:
        print ("account number is incorrect format.")
        return None
    for customer in customers_list:
        if customer.account_number == account_number:
            return customer
    return None

def get_customer_birthday() -> datetime.date:
    year = random.randint(1922,2000)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return datetime.date(year, month,day)

def format_account_number(count:int)-> str:
    count = random.randint(1,10**5)
    return f"1111-{count:010d}"

def selection_sort(customers_list) -> None:
    n = len(customers_list)
    for i in range(n):
        min_vaule = i
        for j  in range (i + 1,n):
            if customers_list[j].account_number < customers_list[min_vaule].account_number:
                min_vaule = j
        customers_list[i],customers_list[min_vaule] = customers_list[min_vaule], customers_list[i]



if __name__ == "__main__":

# Version3: Lägg allt i random order och sortera. 
# se till att det inte blir dubs. Listan ska sorteras efter att man har skapat den.
# måste använda mig av random.randint. Nu är den i random ordning. 
# nu gäller det att få sort att fungera. 
#Klar med sortering. Fick skapa en selection sort
    customers_list = []
    sort_list = []
    start = time()    
    for i in range(10**5):
        customer = Customer(account_number=format_account_number(i), name=str(i), birthday=get_customer_birthday, saldo=int)
        customers_list.append(customer)
        
    
        
    selection_sort(customers_list)

    end = time()
    elapsed_time_for_creating_customers = end - start
    print(f"this is how long it took to create customers: {elapsed_time_for_creating_customers} seconds elsapsed")

    # start = time()
    # result_account1 = find_account(customers,account_number="1111-0000500000")
    # end = time()
    # print ("result: ",result_account1, f" seconds to find {end-start}")

    # start = time()
    # result_account2 = find_account(customers,account_number="1111-0009999999")
    # end= time()
    # print ("result: ",result_account2, f" seconds to find {end-start}")
    
    # start = time()
    # result_account3 = find_account(customers,account_number="1111-9999999999")
    # end = time()
    # print ("result: ",*result_account3, f" seconds to find {end-start}, account does not exist.")