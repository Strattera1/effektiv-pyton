#0.Skapa en generator som yield:ar alla tal som är jämnt delbart på 10, 
#i oändlighet. Dra i snöret i en for-loop eller liknande, som har ett slut (ingen evighetsloop)
from dataclasses import dataclass
from barnum import gen_data
from typing import Iterator

# def modulus_ten(stop):
#     num = 1
#     while True:
#         if num %10 == 0:
#             yield num
#         num +=1
#         if num == stop:
#             break
# for  x in modulus_ten(1000):
#     print(x)

#1. Skapa en funktion som tar en sökväg till en fil (ex bilar.txt) och returnerar alla rader som innehåller  
#minst 3 stycken 'a':n

# def Create_list_of_bilar():
#     with open ("bilar.txt", "a+") as file:
#         bilar = "BMW","VOLVO","LATSABILAR","LADA","FOLKSVAGGN"
#         for _ in bilar:

#             file.write(str(_)+ "\n")
# Create_list_of_bilar()


# def find_car_in_list_with_three_a(filen: str):
#     with open(filen,"r") as file:
#         for bilar in file:
#             if bilar.count("A") >= 3:
#                 yield(bilar.strip())
# # for x in find_car_in_list_with_three_a("bilar.txt"):
# #     print(x)
# def create_fake_person(name:str):
#       with open("fake_person.csv", "a+") as file:
#         file.write(name)
# for x in create_fake_person(10):
#     x(gen_data.create_name())

@dataclass
class Person:
    name: str
    job_title:str
    age:int
    city: str


    